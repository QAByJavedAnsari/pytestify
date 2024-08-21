# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Install Docker (if needed, not typical)
RUN apt-get update && \
    apt-get install -y docker.io

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the Poetry configuration files
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
RUN poetry install --no-dev

# Copy the rest of the application code to the container
COPY . .

# Set PYTHONPATH environment variable
ENV PYTHONPATH=/app/src

# Set environment variable to indicate running inside a Docker container
ENV DOCKER_ENV=true

# Run pytest to execute the tests
CMD ["poetry", "run", "pytest", "-o", "log_cli=True", "-s"]