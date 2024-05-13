# Zen Link - URL Shortener

Zen Link is a simple and user-friendly web-based URL shortening service that allows you to shorten long URLs quickly and easily. With Zen Link, you can create custom shortened links for your URLs, making them easier to share and manage.

## Features

- Shorten long URLs to create compact and easy-to-share links.
- Customize shortened links with user-defined names (e.g., `short.nnisarg.in/my-short-url`).
- Easily copy and share shortened links with others.

## Getting Started

Follow these steps to set up and run Zen Link on your server.

### Prerequisites

- Python 3.x
- Flask (Python web framework)
- pip (Python package manager)

### Installation

Clone the Zen Link repository to your server:

```bash
git clone https://github.com/nnisarggada/zenlink
cd zenlink
```

Create a Python virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate
```

Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Configuration

Edit the Zen Link configuration in the `main.py` file to customize settings such as the hosted URL and the time until links are deleted. Modify the following variables as needed:

```python
URL = "localhost"  # Url of the hosted app
PORT = 5000  # Port on which the app will run (Not for prod)
MINUTES_TO_EXPIRE = 24 * 60  # Number of minutes before a short URL expires (Default is one day)
```

### Running the App

Run the Zen Link app:

```bash
gunicorn -b 0.0.0.0:5000 main:app
```

Here, `5000` is the port on which the app will run. You can access the Zen Link web interface in your web browser at http://localhost:5000.

## Usage

You can use Zen Link to perform the following actions:

### Shorten a URL

1. Enter a long URL in the input field.
2. Optionally, provide a custom short link name.
3. Click "Shorten" to generate a shortened link.

### Share a Shortened URL

Use the provided shortened link to share your original URL. Customize links for easier sharing.

### Delete Links

Shortened links are automatically deleted after the configured time.

### Command-Line Usage (curl/wget)

Zen Link supports URL shortening using command-line tools like curl or wget. For example:

```bash
curl -F "url=example.com" -F "short_url=my-short-url" http://localhost:80/shorten
```

This will shorten the URL `example.com` to http://localhost:80/my-short-url, which will get deleted after the configured time.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions from the community! Please read our [Contribution Guidelines](CONTRIBUTING.md) for details on how to get started.

## Code of Conduct

We maintain a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive environment for all contributors and users.
