import pytest
from .registry_order_validator import registry_order_validator

def test_registry_order_validator():
    body = {
        "data": {
            "name": "Joaozinho",
            "address": "rua do limao",
            "cupom": False,
            "items": [
                { "item": "Refrigerante", "quantidade": 2 },
                { "item": "Pizza", "quantidade": 3 }
            ]
        }
    }
    registry_order_validator(body)

def test__registry_order_validator_with_errors():
    body_with_error = {
        "data": {
            "name": "Joaozinho",
            "address": "rua do limao",
            "cupom": "error",
            "items": [
                { "item": "Refrigerante", "quantidade": 2 },
                { "item": "Pizza", "quantidade": 3 }
            ]
        }
    }
    with pytest.raises(Exception):
        registry_order_validator(body_with_error)
        