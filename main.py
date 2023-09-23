from flask import Flask, render_template, request, redirect, jsonify, abort
import random
import string
import json
import threading
import time
from datetime import datetime, timedelta

# -------------------------------------------------------------------
# The following variables need to be changed before running the app:
# -------------------------------------------------------------------

URL = "localhost" # Url of the hosted app
MINUTES_TO_EXPIRE = 1 # Number of minutes before a short URL expires

# -------------------------------------------------------------------

app = Flask(__name__)

try:
    with open('links_managed.json', 'r') as file:
        url_database = json.load(file)
except FileNotFoundError:
    url_database = {}

def save_to_json():
    with open('links_managed.json', 'w') as file:
        json.dump(url_database, file)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def delete_expired_short_urls():
    while True:

        current_time = datetime.now()
        to_delete = []
        for short_url, data in url_database.items():
            expiration_time = datetime.strptime(data['expiration_time'], '%Y-%m-%d %H:%M:%S')
            if current_time >= expiration_time:
                to_delete.append(short_url)

        for short_url in to_delete:
            del url_database[short_url]

        save_to_json()

        time.sleep(10)

delete_thread = threading.Thread(target=delete_expired_short_urls)
delete_thread.daemon = True
delete_thread.start()


@app.route('/')
def index():
    return render_template('index.html', host_url=URL)

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']

    short_url = request.form.get('short_url', generate_short_url())

    if short_url == "":
        short_url = generate_short_url()

    if not original_url:
        return ('Please provide a URL\n'), 400

    if short_url in url_database or short_url.lower() == "shorten":
        return ('Short URL already exists. Please choose a different one.\n'), 400

    creation_time = datetime.now()
    expiration_time = creation_time + timedelta(minutes=MINUTES_TO_EXPIRE)
    url_database[short_url.lower()] = {
        'original_url': original_url,
        'expiration_time': expiration_time.strftime('%Y-%m-%d %H:%M:%S')
    }

    save_to_json()

    link = f'{URL}/{short_url}\n'
    clickable_link = f'\033]8;;{link}\033\\{link}\033]8;;\033\\'


    user_agent = request.headers.get('User-Agent')
    if 'curl' in user_agent.lower() or 'wget' in user_agent.lower():
        return clickable_link
    else:
        return render_template('shortened.html', url=URL, link=short_url)


@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
    if short_url.lower() in url_database:
        mapping = url_database[short_url.lower()]
        original_url = mapping['original_url']
        if original_url.startswith('http'):
            return redirect(original_url)
        else:
            return redirect('http://' + original_url)
    else:
        return ('Invalid Link\n'), 404

if __name__ == '__main__':
    app.run(debug=True)
