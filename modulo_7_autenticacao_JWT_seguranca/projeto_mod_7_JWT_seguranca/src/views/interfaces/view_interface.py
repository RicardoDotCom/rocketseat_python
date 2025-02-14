from abc import ABC, abstractmethods
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_resonse import HttpResponse

class ViewInterface(ABC):

    @abstractmethods
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass