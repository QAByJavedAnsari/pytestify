import requests
from pytestify.data.data_loader import load_config
from pytestify.utils.utils import send_get_request, send_post_request, send_delete_request, send_put_request

class APIClient:
    def __init__(self, config_file='src/pytestify/config/config.yaml'):
        """
        Initialize the APIClient with a base URL and optional headers from the config file.

        :param config_file: Path to the configuration YAML file.
        """
        config = load_config(config_file)
        self.base_url = config.get('base_url', '').rstrip('/')
        self.headers = config.get('headers', {})

    def _create_url(self, endpoint):
        """
        Create the full URL by combining the base URL and the endpoint.

        :param endpoint: The API endpoint.
        :return: The full URL.
        """
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint, params=None):
        """
        Perform a GET request.

        :param endpoint: The API endpoint.
        :param params: Optional query parameters.
        :return: Response object.
        """
        url = self._create_url(endpoint)
        return send_get_request(url, headers=self.headers, params=params)

    def post(self, endpoint, data=None, json=None):
        """
        Perform a POST request.

        :param endpoint: The API endpoint.
        :param data: Data to send in the body of the request.
        :param json: JSON data to send in the body of the request.
        :return: Response object.
        """
        url = self._create_url(endpoint)
        return send_post_request(url, headers=self.headers, data=data, json=json)

    def put(self, endpoint, data=None, json=None):
        """
        Perform a PUT request.

        :param endpoint: The API endpoint.
        :param data: Data to send in the body of the request.
        :param json: JSON data to send in the body of the request.
        :return: Response object.
        """
        url = self._create_url(endpoint)
        return send_put_request(url, headers=self.headers, data=data, json=json)

    def delete(self, endpoint):
        """
        Perform a DELETE request.

        :param endpoint: The API endpoint.
        :return: Response object.
        """
        url = self._create_url(endpoint)
        return send_delete_request(url, headers=self.headers)