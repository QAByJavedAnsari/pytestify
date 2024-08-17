# Pytestify

**Pytestify** is a base Python testing framework designed to simplify the process of writing and executing tests using `pytest`. It provides a set of utility functions and a configuration setup to get started quickly with testing.

## Features

- **Logging Utilities**: Simple logging functions for informational and error messages.
- **URL Formatting**: Utility to format URLs by combining a base URL and an endpoint.
- **Configuration**: Basic configuration for `pytest` to handle test execution and coverage reporting.

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
For any questions or issues, please contact qabyjavedansari@gmail.com.
