from typing import Dict, List
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
    
class MockDriveHandler:
    def average(self, numbers: List[float]) -> float:
        return 2.5

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4]})
    calculator_4 = Calculator4(MockDriveHandler())
  
    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'average': 2.5}}
    print()
    print(response)