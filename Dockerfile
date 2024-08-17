# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the dependency files to the container
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install poetry

# Install the dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of your application code to the container
COPY . /app/

# Set the default command to run when the container starts
CMD ["poetry", "run", "pytest"]
