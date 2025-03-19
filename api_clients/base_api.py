import requests
from utils.config import Config


class BaseAPI:
    def __init__(self):
        self.base_url = Config.API_URL
        self.base_headers = {
            "Content-Type": "application/json; charset=UTF-8",
        }

    def get(self, endpoint, headers=None):
        """Send a GET request with optional headers."""
        url = f"{self.base_url}{endpoint}"
        headers = headers or self.base_headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response

    def post(self, endpoint, data, headers=None):
        """Send a POST request with optional headers."""
        url = f"{self.base_url}{endpoint}"
        headers = headers or self.base_headers
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response
