import pytest
from src.commands.conditions.strategies.complex_condition import ComplexCondition
from src.dependency_containers.complex_strategy_container import ComplexStrategyContainer

use_cases = [
  {
    "scenario": {'name': '$or', 'value': '{quantity:{$lt:20}},{price:{$lt:10}}'},
    "expected": " ( quantity<\"20\" OR  price<\"10\") ",
  },
  {
    "scenario": {'name': '$and', 'value': '{quantity:{$lt:20}},{price:{$lt:10}}'},
    "expected": " ( quantity<\"20\" AND  price<\"10\") ",
  },  
]

@pytest.mark.parametrize("case", use_cases)
def test_complex_condition(case):
  container = ComplexStrategyContainer()
  command = container.complex_condition_service()
  response = command.execute(case["scenario"])    
  assert response == case["expected"]