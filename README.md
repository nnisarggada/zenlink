# Zen Link - Simple URL Shortener

Zen Link is a lightweight, web-based URL shortening service that allows you to shorten long URLs quickly and easily. With Zen Link, you can create custom shortened links, making it easier to share and manage your URLs.

## Features

- Shorten long URLs to create compact and easy-to-share links.
- Customize shortened links with user-defined names (e.g., `short.nnisarg.in/my-short-url`).
- Automatic deletion of shortened links after a specified time.
- Command-line support for URL shortening via curl or wget.

## Deployment

### Prerequisites

- **Docker** and **Docker Compose** installed on your machine or server.
- A running Docker environment.

### Deployment Using Docker

Zen Link uses **Docker Compose** to manage both the app container and PostgreSQL database container. Deploying the app requires a few simple steps to adjust the configuration.

#### Step 1: Clone the Repository

Clone the Zen Link repository to your local machine or server:

```bash
git clone https://github.com/nnisarggada/zenlink
cd zenlink
```

#### Step 2: Configure `docker-compose.yml`

To configure the deployment, edit the `docker-compose.yml` file and modify the following variables:

- **URL**: Set the `URL` to the domain or IP address where you want the Zen Link app to be accessible (e.g., `"share.nnisarg.in"` or your public domain).
- **MINUTES_TO_EXPIRE**: Set the `MINUTES_TO_EXPIRE` to the number of minutes after which the shortened links will be automatically deleted.
- **NGINX PORT**: Set the `nginx.ports` to the port(s) that you want the NGINX container to listen on.

#### Step 3: Set up the Database

Zen Link uses PostgreSQL as its database, and the database container is configured in the same `docker-compose.yml` file. The default database name, user, and password are already set, but you can modify these if needed.

#### Step 4: Running the Containers

Once you've configured the `docker-compose.yml` file with your desired settings, run the following command to start the containers:

```bash
docker-compose up --build -d
```

This command will:

- Build the app container.
- Start the PostgreSQL container.
- Start the app container.
- Start the NGINX container.

### Scaling the Application

Zen Link is designed to scale horizontally by adding more app containers. You can dynamically scale the app containers using Docker Compose.

#### Step 1: Scale the Application Containers

You can change the number of replicas of the app service by modifying the `docker-compose.yml` file or by using the following command:

```bash
docker-compose up --scale app=3 -d
```

This command will scale the `app` service to 3 replicas. The number of app replicas can be adjusted dynamically based on your traffic.

To scale the app containers while they are running, you can use the `docker-compose scale` command:

```bash
docker-compose scale app=3
```

### Access the App

Once the containers are running, you can access Zen Link in your web browser at the domain or IP address you specified in the `URL` variable. If you mapped port 8080, the app will be accessible at `http://localhost:8080`.

---

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
curl -F "url=example.com" -F "short_url=my-short-url" http://localhost:8080/shorten
```

This will shorten the URL `example.com` to [http://localhost:8080/my-short-url](http://localhost:8080/my-short-url), which will get deleted after the configured time.

---

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
