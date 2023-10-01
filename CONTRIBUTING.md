# Contributing to Zen Link - URL Shortener

Thank you for your interest in contributing to Zen Link! We welcome your contributions to help improve our simple and user-friendly web-based URL shortening service. This document outlines the guidelines for contributing to the project. Please read and follow these guidelines to ensure a smooth and collaborative development process.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Submitting Changes](#submitting-changes)
- [Development Setup](#development-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the App](#running-the-app)

## Code of Conduct

Before contributing, please review our [Code of Conduct](CODE_OF_CONDUCT.md). We expect all contributors to adhere to this code to maintain a welcoming and inclusive community.

## How Can I Contribute?

### Reporting Bugs

If you encounter a bug while using Zen Link or have identified a potential issue, please [open a new issue](https://github.com/nnisarggada/zenlink/issues/new) on our GitHub repository. Ensure that your report includes detailed information about the problem, such as the steps to reproduce it and any relevant error messages.

### Suggesting Enhancements

If you have ideas for new features or improvements to existing ones, feel free to [create an enhancement request](https://github.com/nnisarggada/zenlink/issues/new) on GitHub. Be clear and specific about the proposed enhancement and how it would benefit Zen Link.

### Submitting Changes

If you'd like to contribute code to Zen Link, follow these steps:

1. Fork the Zen Link repository on GitHub.
2. Create a new branch from the `main` branch to work on your changes.
3. Make your changes and ensure that they follow the project's coding standards.
4. Test your changes thoroughly.
5. Create a pull request (PR) describing your changes, explaining their purpose, and providing steps for testing.
6. Be prepared to respond to feedback and make necessary adjustments.

## Development Setup

To set up a development environment for Zen Link, follow these steps:

### Prerequisites

Ensure you have the following prerequisites installed:

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
MINUTES_TO_EXPIRE = 1  # Number of minutes before a short URL expires
```

### Running the App

Run the Zen Link app:

```bash
gunicorn -b 0.0.0.0:80 main:app
```

Here, `80` is the port on which the app will run. You can access the Zen Link web interface in your web browser at http://localhost:80.
