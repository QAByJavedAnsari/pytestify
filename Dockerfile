# Use the official Python image from the Docker Hub
FROM python:3.12-slim

## Install Docker (if needed, not typical)
#RUN apt-get update && \
#    apt-get install -y docker.io

# Install dependencies for Allure CLI
RUN apt-get update && \
    apt-get install -y unzip curl

# Install Allure CLI
RUN curl -o allure-commandline.zip -L "https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.9/allure-commandline-2.13.9.zip" && \
    unzip allure-commandline.zip -d /opt/ && \
    ln -s /opt/allure-2.13.9/bin/allure /usr/bin/allure

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the Poetry configuration files
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
RUN poetry install --with dev

# Copy the rest of the application code to the container
COPY . .

# Set PYTHONPATH environment variable
ENV PYTHONPATH=/app/src

# Run linting (optional: uncomment if you want linting to run during build)
#RUN poetry run pylint src/

# Set environment variable to indicate running inside a Docker container
ENV DOCKER_ENV=true



# Run linting (optional)
# RUN poetry run pylint src/


# Run pytest to execute the tests and generate allure results
CMD ["sh", "-c", "poetry run pytest --alluredir=allure-results --log-cli-level=INFO -s && allure serve allure-results"]