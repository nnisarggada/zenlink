# Zen Link - Simple URL Shortener

Zen Link is a lightweight, web-based URL shortening service that allows you to shorten long URLs quickly and easily. With Zen Link, you can create custom shortened links, making it easier to share and manage your URLs.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running with Docker](#running-with-docker)
- [Usage](#usage)
  - [Shorten a URL](#shorten-a-url)
  - [Share a Shortened URL](#share-a-shortened-url)
  - [Delete Links](#delete-links)
  - [Command-Line Usage (curl/wget)](#command-line-usage-curlwget)
- [TODO](#todo)
- [License](#license)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)

## Features

- Shorten long URLs to create compact and easy-to-share links.
- Customize shortened links with user-defined names (e.g., `short.nnisarg.in/my-short-url`).
- Automatic deletion of shortened links after a specified time.
- Command-line support for URL shortening via curl or wget.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.x (for development purposes if you want to run the app outside Docker)

### Installation

Clone the Zen Link repository to your server:

```bash
git clone https://github.com/nnisarggada/zenlink
cd zenlink
```

### Configuration

If you wish to modify configuration settings like the base URL (`URL`), port (`PORT`), and expiration time (`MINUTES_TO_EXPIRE`), you can do so in the `docker-compose.yml` file under the `environment` section. The default values are:

```yaml
app:
  environment:
    URL: "share.nnisarg.in" # Base URL of the hosted app
    PORT: 5000 # Port on which the app will run (Not for prod)
    MINUTES_TO_EXPIRE: 1440 # Number of minutes before a short URL expires (Default is one day)
    DB_HOST: db # PostgreSQL container name
    DB_PORT: 5432 # Default PostgreSQL port
    DB_NAME: zenlink # PostgreSQL database name
    DB_USER: user # PostgreSQL database user
    DB_PASSWORD: password # PostgreSQL database password
```

### Running with Docker

Zen Link uses Docker and Docker Compose to run both the Flask application and PostgreSQL in containers. Follow these steps to get started:

1. **Build and Start the Docker Containers:**

   First, ensure that Docker and Docker Compose are installed. Then, run the following command to build the containers and start the app and database:

   ```bash
   docker-compose up --build
   ```

2. **Access the App:**

   After the containers have started, you can access the Zen Link app by visiting [http://localhost:5000](http://localhost:5000) in your web browser. The app will be running on port `5000`.

3. **Stop the Containers:**

   To stop the containers, use the following command:

   ```bash
   docker-compose down
   ```

4. **Health Check:**

   The PostgreSQL container has a health check configured, which ensures that it is ready before the app container starts. If the health check fails, Docker will retry until PostgreSQL is available.

## Usage

Zen Link supports the following features:

### Shorten a URL

1. Enter a long URL in the input field.
2. Optionally, provide a custom short link name.
3. Click "Shorten" to generate a shortened link.

### Share a Shortened URL

Use the provided shortened link to share your original URL. Customize links for easier sharing.

### Delete Links

Shortened links are automatically deleted after the configured time (default: 1 day).

### Command-Line Usage (curl/wget)

Zen Link supports URL shortening using command-line tools like curl or wget. For example:

```bash
curl -F "url=example.com" -F "short_url=my-short-url" http://localhost:5000/shorten
```

This will shorten the URL `example.com` to [http://localhost:5000/my-short-url](http://localhost:5000/my-short-url), which will get deleted after the configured time.

## TODO

- [ ] Add rate limiting.
- [ ] Add logging for URL creation and access.
- [ ] Develop an admin dashboard for managing shortened URLs and monitoring usage.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions from the community! Please read our [Contribution Guidelines](CONTRIBUTING.md) for details on how to get started.

## Code of Conduct

We maintain a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive environment for all contributors and users.
