# Use Python 3.9 image as base
FROM python:3.9-slim

# Set environment variables to avoid writing .pyc files and to disable buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements.txt file
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["gunicorn" , "--bind", "0.0.0.0:5000", "main:app"]
