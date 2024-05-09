from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
        return 3

def test_calculate():
    mock_request = MockRequest({"numbers": [1,2,3,4,5]})

    driver = MockDriverHandler()
    calculator_4 = Calculator4(driver)
    formated_result = calculator_4.calculate(mock_request)

    assert isinstance(formated_result, dict)
    assert formated_result == {'data': {'Calculator': 4, 'result': 3}}


