import pytest

from src.commands.conditions.strategies.simple_condition import SimpleCondition

# from src.dependency_containers.wheres_container import WheresContainer

use_cases = [
    {
        "scenario": {"name": "name", "value": "$ne:julio"},
        "expected": ' name!="julio"',
    },
    {
        "scenario": {"name": "_id", "value": "23113"},
        "expected": ' id="23113"',
    },
    {
        "scenario": {"name": "first_name", "value": "Marcos"},
        "expected": ' first_name="Marcos"',
    },
    {
        "scenario": {"name": "first_name", "value": "Marcos"},
        "expected": ' first_name="Marcos"',
    },
    {
        "scenario": {"name": "qty", "value": "$in:[5,15]"},
        "expected": " qty IN (5,15)",
    },
    {
        "scenario": {"name": "center", "value": "$eq:Came"},
        "expected": ' center="Came"',
    },
]


@pytest.mark.parametrize("case", use_cases)
def test_simple_condition(case):
    command = SimpleCondition()
    response = command.execute(case["scenario"])
    assert response == case["expected"]
