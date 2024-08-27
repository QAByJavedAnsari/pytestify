# src/pytestify/client/cpi_client.py
import logging

import requests
#from jaraco.functools import retry

from pytestify.data.data_loader import load_config
from pytestify.utils.utils import send_get_request, send_post_request, send_delete_request, send_put_request, retry_request

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url=None, config_file='src/pytestify/config/config.yaml'):
        """
        Initialize the APIClient with a base URL and optional headers.
        :param base_url: Base URL for the API client. If None, uses the config file.
        :param config_file: Path to the configuration YAML file.
        """
        self.headers = {}  # Initialize headers to an empty dictionary
        if base_url:
            self.base_url = base_url.rstrip('/')
        else:
            config = load_config(config_file)
            self.base_url = config.get('base_url', '').rstrip('/')
            self.headers = config.get('headers', {})
        self.session = requests.Session()  # Initialize a session to manage connections
        logger.info(f"Initialized APIClient with base URL: {self.base_url}")

    def reload_config(self, config_file='src/pytestify/config/config.yaml'):
        """
        Reload configuration from a new config file.
        :param config_file: Path to the new configuration YAML file.
        """
        config = load_config(config_file)
        self.base_url = config.get('base_url', '').rstrip('/')
        self.headers = config.get('headers', {})
        logger.info(f"Reloaded APIClient configuration with base URL: {self.base_url}")

    def _create_url(self, endpoint):
        """
        Create the full URL by combining the base URL and the endpoint.

        :param endpoint: The API endpoint.
        :return: The full URL.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.debug(f"Created URL: {url}")
        return url


    def get(self, endpoint, params=None):
        """
        Perform a GET request.

        :param endpoint: The API endpoint.
        :param params: Optional query parameters.
        :return: Response object.
        """
        url = self._create_url(endpoint)
        logger.info(f"Performing GET request to {url} with params: {params}")
        response = retry_request(lambda: send_get_request(self.session, url, headers=self.headers, params=params))

        if response is None:
            logger.error(f"GET request to {url} failed and returned None")
        else:
            logger.info(f"GET request to {url} returned status code {response.status_code}")

        return response

    def post(self, endpoint, data=None, json=None):
        """
        Perform a POST request.

        :param endpoint: The API endpoint.
        :param data: Data to send in the body of the request.
        :param json: JSON data to send in the body of the request.
        :return: Response object.
        """
        url = self._create_url(endpoint)
        logger.info(f"Performing POST request to {url} with data: {data} and json: {json}")
        response = retry_request(
            lambda: send_post_request(self.session, url, headers=self.headers, data=data, json=json))

        if response is None:
            logger.error(f"POST request to {url} failed and returned None")
        else:
            logger.info(f"POST request to {url} returned status code {response.status_code}")

        return response


    def put(self, endpoint, data=None, json=None):
        """
        Perform a PUT request.

        :param endpoint: The API endpoint.
        :param data: Data to send in the body of the request.
        :param json: JSON data to send in the body of the request.
        :return: Response object.
        """
        url = self._create_url(endpoint)
        logger.info(f"Performing PUT request to {url} with data: {data} and json: {json}")
        response = retry_request(
            lambda: send_put_request(self.session, url, headers=self.headers, data=data, json=json))

        if response is None:
            logger.error(f"PUT request to {url} failed and returned None")
        else:
            logger.info(f"PUT request to {url} returned status code {response.status_code}")

        return response


    def delete(self, endpoint):
        """
        Perform a DELETE request.

        :param endpoint: The API endpoint.
        :return: Response object.
        """
        url = self._create_url(endpoint)
        logger.info(f"Performing DELETE request to {url}")
        response = retry_request(lambda: send_delete_request(self.session, url, headers=self.headers))

        if response is None:
            logger.error(f"DELETE request to {url} failed and returned None")
        else:
            logger.info(f"DELETE request to {url} returned status code {response.status_code}")

        return response


    def close(self):
        """
        Close the session to free up resources.
        """
        self.session.close()
        logger.info("Closed APIClient session")