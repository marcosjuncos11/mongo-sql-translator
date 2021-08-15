import pytest

from src.commands.conditions.conditions import Conditions
from src.dependency_containers.conditions_container import ConditionsContainer

use_cases = [
    {
        "scenario": [{"name": "name", "value": "julio"}],
        "expected": ' name="julio"',
    },
    {
        "scenario": [{"name": "_id", "value": "23113"}],
        "expected": ' id="23113"',
    },
    {
        "scenario": [{"name": "first_name", "value": "Marcos"}],
        "expected": ' first_name="Marcos"',
    },
    {
        "scenario": [
            {"name": "first_name", "value": "Marcos"},
            {"name": "last_name", "value": "Juncos"},
        ],
        "expected": ' first_name="Marcos" AND  last_name="Juncos"',
    },
    {
        "scenario": [{"name": "$or", "value": "{quantity:{$lt:20}},{price:{$lt:10}}"}],
        "expected": ' ( quantity<"20" OR  price<"10") ',
    },
    {
        "scenario": [{"name": "$and", "value": "{quantity:{$lt:20}},{price:{$lt:10}}"}],
        "expected": ' ( quantity<"20" AND  price<"10") ',
    },
    {
        "scenario": [{"name": "qty", "value": "$in:[5,15]"}],
        "expected": " qty IN (5,15)",
    },
    {
        "scenario": [{"name": "qty", "value": "$gte:15"}],
        "expected": ' qty>="15"',
    },
    {
        "scenario": [
            {"name": "center", "value": "$eq:Came"},
            {"name": "homepage_featured", "value": "$ne:0"},
        ],
        "expected": ' center="Came" AND  homepage_featured!="0"',
    },
]


@pytest.mark.parametrize("case", use_cases)
def test_conditions(case):
    container = ConditionsContainer()
    command = container.conditions_service()
    response = command.execute(case["scenario"])
    # print(response)
    assert response == case["expected"]
