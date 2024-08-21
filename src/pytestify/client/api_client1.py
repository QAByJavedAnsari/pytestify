# src/pytestify/client/api_client.py

import logging
from pytestify.utils.utils import send_get_request, send_post_request, send_put_request, send_delete_request, retry_request
from pytestify.data.data_loader import load_config

class APIClient:
    def __init__(self, config_file='src/pytestify/config/config.yaml'):
        """
        Initialize the APIClient with a base URL and optional headers from the config file.
        """
        config = load_config(config_file)
        self.base_url = config.get('base_url', '').rstrip('/')
        self.headers = config.get('headers', {})

    def _create_url(self, endpoint):
        """
        Create the full URL by combining the base URL and the endpoint.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint, params=None):
        """
        Perform a GET request.
        """
        url = self._create_url(endpoint)
        response = retry_request(send_get_request, url, headers=self.headers, params=params)
        logging.info(f"GET {url} with params {params} returned status {response.status_code}")
        return response

    def post(self, endpoint, data=None, json=None):
        """
        Perform a POST request.
        """
        url = self._create_url(endpoint)
        response = retry_request(send_post_request, url, headers=self.headers, data=data, json=json)
        logging.info(f"POST {url} with data {data} and json {json} returned status {response.status_code}")
        return response

    def put(self, endpoint, data=None, json=None):
        """
        Perform a PUT request.
        """
        url = self._create_url(endpoint)
        response = retry_request(send_put_request, url, headers=self.headers, data=data, json=json)
        logging.info(f"PUT {url} with data {data} and json {json} returned status {response.status_code}")
        return response

    def delete(self, endpoint):
        """
        Perform a DELETE request.
        """
        url = self._create_url(endpoint)
        response = retry_request(send_delete_request, url, headers=self.headers)
        logging.info(f"DELETE {url} returned status {response.status_code}")
        return response

    def close(self):
        """
        Close the API client session.
        """
        # If there are resources to close, handle them here
        pass
