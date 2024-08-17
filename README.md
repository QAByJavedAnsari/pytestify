# Pytestify

**Pytestify** is a Python testing framework that enhances pytest by offering utility functions and streamlined configurations. It simplifies writing, executing, and managing tests, making it easier to achieve robust and reliable testing outcomes.

## Features

- **Enhanced Logging Utilities**: Comprehensive logging functions for various levels, including info, warning, error, and critical.
- **Flexible URL Formatting**: Utility to dynamically format URLs with parameters, combining a base URL and endpoint.
- **Schema Validation**: Built-in support for JSON schema validation to ensure data integrity and compliance.
- **Advanced Comparison**: Recursive JSON comparison to identify discrepancies between expected and actual data.
- **Configuration Management**: Centralized configuration using YAML files for base URLs, endpoints, and schemas, streamlining test setups.
- **Robust Test Utilities**: Functions for managing retries, logging response times, and handling HTTP operations (GET, POST, PUT, DELETE).


## Installation

To use `pytestify`, you need to have Python 3.12 or higher installed. You can set up the environment and install dependencies using `Poetry`.

1. **Clone the Repository**:
   ```bash
   git clone <REPOSITORY_URL>
   cd <REPOSITORY_NAME>

2. **Install Dependencies**:
   curl -sSL https://install.python-poetry.org | python3 -
   poetry install

3. **Activate the Virtual Environment**:
   poetry shell

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
   To run tests and generate a coverage report, use:
```BASH   
    pytest --cov=src/pytestify --cov-report=term-missing
    pytest
```
3. **Configuration**:
   The pytest.ini file is located in the root directory and is used to configure pytest options:
```BASH
    [pytest]
    addopts = --maxfail=5 --disable-warnings -q
    testpaths =
          src/pytestify/tests
````
4. **Development**:
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


## License
This project is licensed under the MIT License - see the LICENSE file for details.


## Contact
For any questions or issues, please contact qabyjavedansari@gmail.com OR connect with me over linked on www.linkedin.com/in/qaleaderjavedansari.
