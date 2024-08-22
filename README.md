# Pytestify

**Pytestify** is a Python testing framework that enhances pytest by offering utility functions and streamlined configurations. It simplifies writing, executing, and managing tests, making it easier to achieve robust and reliable testing outcomes.

## Features

- **Enhanced Logging Utilities**: Comprehensive logging functions for various levels, including info, warning, error, and critical.
- **Flexible URL Formatting**: Utility to dynamically format URLs with parameters, combining a base URL and endpoint.
- **Schema Validation**: Built-in support for JSON schema validation to ensure data integrity and compliance.
- **Advanced Comparison**: Recursive JSON comparison to identify discrepancies between expected and actual data.
- **Configuration Management**: Centralized configuration using YAML files for base URLs, endpoints, and schemas, streamlining test setups.
- **Robust Test Utilities**: Functions for managing retries, logging response times, and handling HTTP operations (GET, POST, PUT, DELETE).
- **Docker Integration**: Build and run tests within Docker containers.
- **Session Management**: Check Docker status and manage Docker sessions.


## Installation

To use `pytestify`, you need to have Python 3.12 or higher installed. You can set up the environment and install dependencies using `Poetry`.

1. **Clone the Repository**:
   ```bash
   git clone <REPOSITORY_URL>
   cd <REPOSITORY_NAME>

2. **Install Dependencies**:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   poetry install
   ```

3. **Activate the Virtual Environment**:
   ```
   poetry shell
   ```

## Docker Requirements

Docker is required to run the tests using the provided Docker image. Make sure Docker is installed and running on your machine. If Docker is not installed, follow the installation guide for your operating system:

- [Docker Installation Guide](https://docs.docker.com/get-docker/)

### Starting Docker

If Docker is not running, you can start it by following these steps:

- **For macOS**: Open the Docker Desktop application.
- **For Windows**: Open Docker Desktop from the Start menu.
- **For Linux**: Run `sudo systemctl start docker` in the terminal.

### Troubleshooting

If you encounter errors related to Docker not running, make sure Docker is properly installed and the Docker daemon is active.

## Checking Docker Status

Before running Docker commands, you can check if Docker is running by executing the following Python script:

```bash
python scripts/check_docker.py
```

## Usage

1. **Writing Tests**:
   You can create test files under the src/pytestify/tests directory. Here’s a basic example:
###### src/pytestify/tests/sample_test.py
```bash    
    from pytestify.utils.utils import log_info, format_url
        
    def test_format_url():
    base_url = "http://example.com"
    endpoint = "api/test"
    expected = "http://example.com/api/test"
    assert format_url(base_url, endpoint) == expected
    
    def test_log_info(caplog):
    log_info("Test message")
    assert "INFO: Test message" in caplog.text    
```
2. **Running Tests**:
- Use Poetry to run tests and generate a coverage report:
   ```bash
     poetry run pytest
     ```
   - Or, use pytest directly:
```BASH   
    pytest --cov=src/pytestify --cov-report=term-missing
```
## Running Tests with Docker

You can run the tests in a Docker container by building and running the Docker image.

### Build the Docker Image

```bash
docker build -t pytestify:latest .
````
### Run Tests Using Docker
```
docker run --rm pytestify:latest
```
### Running Tests Without Docker

If you do not want to use Docker, you can run the tests directly using Poetry. Follow these steps:

1. **Install Dependencies**

    ```bash
    poetry install
    ```

2. **Run Tests**

    ```bash
    poetry run pytest
    ```
## Configuration:
   The pytest.ini file is located in the root directory and is used to configure pytest options:
```BASH
    [pytest]
    addopts = --maxfail=5 --disable-warnings -q
    testpaths =
          src/pytestify/tests
````

## **Contribution Guidelines**:
    To contribute to the development of pytestify, follow these steps:
   - **Create a New Branch**:
       ```BASH
         git checkout -b feature/my-feature
       ```
   - **Make Your Changes**:
        Edit code and write tests as needed.
- 
  - **Commit Your Changes**:
      ```BASH
      git add .
      git commit -m "Add new feature or fix bug"
      ```
  - **Push Your Changes**:
      ```BASH
      git push origin feature/my-feature
      ```
  - **Create a Pull Request**:
        Open a pull request on the repository to merge your changes.

## WireMock Integration

### Setting Up WireMock

To test your APIs using WireMock:

1. **Directory Structure**:
   - Place your WireMock mappings in the `wiremock/mappings` directory.
   - Place your response files in the `wiremock/__files` directory.

2. **Running WireMock**:
   - WireMock can be started and stopped automatically using `pytest` fixtures. See [conftest.py](./src/pytestify/tests/conftest.py) for details.

3. **Writing Tests**:
   - Use `requests` to interact with the mock server. Ensure that your tests handle different scenarios such as varying responses and status codes.

### Example Test

```python
import requests

def test_sample_response():
    response = requests.get("http://localhost:8080/api/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Sample response from WireMock"}
```

### Summary

- **Automate Setup**: Use `pytest` fixtures to manage WireMock lifecycle.
- **Enhance Coverage**: Add more tests and mappings.
- **CI/CD Integration**: Configure your CI/CD pipeline to handle WireMock.
- **Update Documentation**: Provide clear instructions on using WireMock.

If you need help with any of these steps or have additional questions, let me know!



## API Documentation

### APIClient Class
- get(url, headers=None, params=None): Sends a GET request.
  -  Parameters:
     - url: The URL to send the request to. 
     - headers: Optional headers to include in the request. 
     - params: Optional parameters to include in the request. 
  - Returns: Response object.
- post(url, headers=None, data=None, json=None): Sends a POST request.
  - Parameters:
    - url: The URL to send the request to. 
    - headers: Optional headers. 
    - data: Optional data to send in the request body. 
    - json: Optional JSON to send in the request body.
  - Returns: Response object. 

## Utility Functions
- format_url(base_url, endpoint): Combines a base URL and endpoint.
- validate_json_schema(response_json, schema): Validates JSON response against a schema.
- compare_json(expected, actual, path=""): Compares two JSON objects recursively. 
- load_schema(file_path='src/pytestify/config/schema_config.yaml'): Loads JSON schema from a YAML file.



## License
This project is licensed under the MIT License - see the LICENSE file for details.


## Contact
For any questions or issues, please contact qabyjavedansari@gmail.com OR connect with me over linked on www.linkedin.com/in/qaleaderjavedansari.
