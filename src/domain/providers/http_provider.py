from abc import ABC, abstractmethod

from requests import Response


class HttpProvider(ABC):
    @abstractmethod
    def get(self, url: str) -> Response:
        pass