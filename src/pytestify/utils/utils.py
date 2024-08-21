import logging
import time
import requests
import yaml
from jsonschema import validate, ValidationError

def log_info(message):
    """Log an informational message."""
    logging.info(message)

def log_warning(message):
    """Log a warning message."""
    logging.warning(message)

def log_error(message):
    """Log an error message."""
    logging.error(message)

def log_critical(message):
    """Log a critical error message."""
    logging.critical(message)

def format_url(base_url, endpoint):
    """Format URL by combining base URL and endpoint."""
    if base_url is None or endpoint is None:
        log_error("Base URL or endpoint is None")
        return None
    return f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

def validate_json_schema(response_json, schema):
    """Validate a JSON response against a schema."""
    try:
        validate(instance=response_json, schema=schema)
        log_info("JSON schema validation passed.")
        return True
    except ValidationError as e:
        log_error(f"JSON schema validation failed: {e.message}")
        return False

def send_get_request(session, url, headers=None, params=None):
    response = session.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response

def send_post_request(session, url, headers=None, data=None, json=None):
    response = session.post(url, headers=headers, data=data, json=json)
    response.raise_for_status()
    return response

def send_put_request(session, url, headers=None, data=None, json=None):
    response = session.put(url, headers=headers, data=data, json=json)
    response.raise_for_status()
    return response

def send_delete_request(session, url, headers=None):
    response = session.delete(url, headers=headers)
    response.raise_for_status()
    return response

def log_response_time(request_func, *args, **kwargs):
    """Logs the response time of an API request."""
    start_time = time.time()
    response = request_func(*args, **kwargs)
    end_time = time.time()
    log_info(f"Response time: {end_time - start_time:.2f} seconds")
    return response

def retry_request(request_func, retries=3, *args, **kwargs):
    """Retries an API request in case of failure."""
    for attempt in range(retries):
        try:
            response = request_func(*args, **kwargs)
            if response.ok:
                return response
        except requests.RequestException as e:
            log_warning(f"Request failed: {e}. Retrying... ({attempt+1}/{retries})")
    log_critical(f"Request failed after {retries} attempts.")
    return None

def compare_json(expected, actual, path=""):
    """
    Recursively compare two JSON objects and return differences.
    """
    differences = []
    if isinstance(expected, dict) and isinstance(actual, dict):
        for key in expected:
            if key not in actual:
                differences.append(f"Key '{key}' is missing in actual data at '{path}'")
            else:
                differences.extend(compare_json(expected[key], actual[key], path + "." + key))
    elif isinstance(expected, list) and isinstance(actual, list):
        for index, item in enumerate(expected):
            if index < len(actual):
                differences.extend(compare_json(item, actual[index], path + f"[{index}]"))
            else:
                differences.append(f"Index {index} is missing in actual data at '{path}'")
    else:
        if expected != actual:
            differences.append(f"Mismatch at '{path}': expected {expected}, got {actual}")
    return differences

def get_json_attribute(data, path):
    """
    Fetch a specific attribute from a JSON object using a path.
    Example path: "user.address.street"
    """
    keys = path.split('.')
    for key in keys:
        data = data.get(key, {})
    return data


def extract_values_from_json_array(data, key):
    """
    Extracts a list of values from an array of JSON objects.
    Example: [{"name": "John"}, {"name": "Doe"}], key="name" returns ["John", "Doe"]
    """
    return [item.get(key) for item in data if key in item]

def load_schema(file_path='src/pytestify/config/schema_config.yaml'):
    """Load the JSON schema from the YAML configuration file."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)