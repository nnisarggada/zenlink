from datetime import datetime, timedelta
import random
import string
import threading
import time
import psycopg2
from flask import Flask, redirect, render_template, request
from dotenv import load_dotenv
import os

_ = load_dotenv()

# -------------------------------------------------------------------
# The following variables are now loaded from the .env file:
# -------------------------------------------------------------------

URL = os.getenv("URL", "short.nnisarg.in")  # URL of the hosted app
PORT = int(os.getenv("PORT", 5000))  # PORT of the hosted app
# Expiration time in minutes
MINUTES_TO_EXPIRE = int(os.getenv("MINUTES_TO_EXPIRE", 24 * 60))
DB_HOST = os.getenv("DB_HOST", "localhost")  # PostgreSQL database hostname
DB_PORT = int(os.getenv("DB_PORT", 5432))  # PostgreSQL database port
DB_NAME = os.getenv("DB_NAME", "zenlink")  # PostgreSQL database name
DB_USER = os.getenv("DB_USER", "user")  # PostgreSQL database user
# PostgreSQL database password
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

# -------------------------------------------------------------------

app = Flask(__name__)


# Connect to PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    return conn


# Create the URLs table if it doesn't exist
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS urls (
            short_url TEXT PRIMARY KEY,
            original_url TEXT NOT NULL,
            expiration_time TIMESTAMP NOT NULL
        );
    """
    )
    conn.commit()
    cur.close()
    conn.close()


def generate_short_url():
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(6))


def delete_expired_short_urls():
    while True:
        current_time = datetime.now()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT short_url, expiration_time FROM urls")
        urls: list[tuple[str, datetime]] = cur.fetchall()

        to_delete: list[str] = []
        for short_url, expiration_time in urls:
            if current_time >= expiration_time:
                to_delete.append(short_url)

        for short_url in to_delete:
            cur.execute("DELETE FROM urls WHERE short_url = %s", (short_url,))

        conn.commit()
        cur.close()
        conn.close()
        time.sleep(10)  # Check every 10 seconds


@app.route("/")
def index():
    return render_template("index.html", host_url=URL)


@app.route("/", methods=["POST"])
def shorten():
    original_url = request.form["url"]

    short_url = request.form.get("short_url", generate_short_url())

    if short_url == "":
        short_url = generate_short_url()

    if not original_url:
        return ("Please provide a URL\n"), 400

    conn = get_db_connection()
    cur = conn.cursor()

    # Check if the short URL already exists
    cur.execute("SELECT * FROM urls WHERE short_url = %s", (short_url.lower(),))
    existing_url = cur.fetchone()

    if existing_url or short_url.lower() == "about":
        cur.close()
        conn.close()
        return ("Short URL already exists. Please choose a different one.\n"), 400

    # Insert the new URL mapping
    creation_time = datetime.now()
    expiration_time = creation_time + timedelta(minutes=MINUTES_TO_EXPIRE)
    cur.execute(
        """
        INSERT INTO urls (short_url, original_url, expiration_time)
        VALUES (%s, %s, %s)
    """,
        (short_url.lower(), original_url, expiration_time),
    )

    conn.commit()
    cur.close()
    conn.close()

    user_agent = request.headers.get("User-Agent")
    if not user_agent:
        user_agent = "Unknown"

    if "curl" in user_agent.lower() or "wget" in user_agent.lower():
        return "https://" + URL + "/" + short_url + "\n"
    else:
        return render_template("success.html", url=URL, link=short_url)


@app.route("/<short_url>", methods=["GET"])
def redirect_to_original(short_url: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT original_url FROM urls WHERE short_url = %s", (short_url.lower(),)
    )
    result = cur.fetchone()
    cur.close()
    conn.close()

    if not result:
        return ("Invalid Link\n"), 404

    original_url: str = result[0]
    if original_url.startswith("http"):
        return redirect(original_url)
    else:
        return redirect("http://" + original_url)


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", full_url=URL)


if __name__ == "__main__":
    create_table()
    delete_thread = threading.Thread(target=delete_expired_short_urls)
    delete_thread.daemon = True
    delete_thread.start()
    app.run(host="0.0.0.0", port=PORT)
