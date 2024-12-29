import requests
from requests import Response

from src.domain.providers.http_provider import HttpProvider


class HttpAdapter(HttpProvider):
    def get(self, url: str) -> Response:
        response = requests.get(url)

        return response
