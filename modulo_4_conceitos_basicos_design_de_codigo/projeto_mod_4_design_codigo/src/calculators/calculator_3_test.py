from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriveHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3
    
class MockDriveHandler:
    def variance(self, numbers: List[float]) -> float:
        return 1000000

def test_calculate_with_variance_erro():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriveHandlerError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)
  
    assert str(excinfo.value) == 'Falha no processo: Variância menor que multiplicação'

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriveHandler())
  
    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'Calculator': 3, 'Value': 1000000, 'Sucess': True}}
    print()
    print(response)