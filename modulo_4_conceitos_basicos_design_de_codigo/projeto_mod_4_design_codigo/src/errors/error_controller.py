from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError
from typing import Dict

def handler_errors(error : Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        }
    return {
        "status_code": 500,
        "body": [{
            "errors": "Server Error" ,
            "detail": str(error)
        }]
    }
