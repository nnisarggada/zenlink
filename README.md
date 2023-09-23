# Zen Link - URL Shortener

Zen Link is a simple and user-friendly web-based URL shortening service that allows you to shorten long URLs quickly and easily. With Zen Link, you can create custom shortened links for your URLs, making them easier to share and manage.

## Features

- Shorten long URLs to create compact and easy-to-share links.
- Customize shortened links with user-defined names (e.g., short.nnisarg.in/my-short-url).
- Easily copy and share shortened links with others.

## Getting Started

Follow these steps to set up and run Zen Link on your server.

### Prerequisites

- Python 3.x
- Flask (Python web framework)
- pip (Python package manager)

### Installation

```bash
# Clone the Zen Link repository to your server
git clone https://github.com/yourusername/zen-link

# Navigate to the project directory
cd zen-link

# Create a Python virtual environment and activate it
python -m venv env
source env/bin/activate

# Install the required dependencies from the requirements.txt file
pip install -r requirements.txt
```

### Configuration

1. Edit the Zen Link configuration in the `main.py` file to customize settings such as the hosted URL and the time until links are deleted.

```python

URL = "localhost" # Url of the hosted app
MINUTES_TO_EXPIRE = 1 # Number of minutes before a short URL expires

```

### Running the App

1. Run the Zen Link app:

```bash
gunicorn -b 0.0.0.0:80 main:app
```

Here, `80` is the port on which the app will run.

2. Access the Zen Link web interface in your web browser:

   ```
   http://localhost:80
   ```

### Usage

1. Shorten a URL:

   - Enter a long URL in the input field.
   - Optionally, provide a custom short link name.
   - Click "Shorten" to generate a shortened link.

2. Share a Shortened URL:

   - Use the provided shortened link to share your original URL.
   - Customize links for easier sharing.

3. Delete Files:

   - Uploaded files are automatically deleted after the configured time.

4. Command-Line Usage (curl/wget):

   - Zen Link supports URL shortening using command-line tools like curl or wget. For example,

     ```bash
     curl -X POST -F "url=example.com" -F "link=my-short-url" http://localhost:80/shorten
     ```

     This will shorten the URL `example.com` to a `http://localhost:80/my-short-url` that will get deleted after the configured time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
