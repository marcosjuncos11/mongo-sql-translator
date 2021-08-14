import pytest
from src.commands.wheres.wheres import Wheres
from src.dependency_containers.wheres_container import WheresContainer

use_cases = [
    {
        "scenario": "{name:'julio'}",
        "expected": [{"name": "name", "value": "julio"}],
    },
    {
        "scenario": "{_id:23113}",
        "expected": [{"name": "_id", "value": "23113"}],
    },
    {
        "scenario": '{ first_name: "Marcos"}',
        "expected": [{"name": "first_name", "value": "Marcos"}],
    },
    {
        "scenario": '{ first_name: "Marcos", last_name: "Juncos"}',
        "expected": [
            {"name": "first_name", "value": "Marcos"},
            {"name": "last_name", "value": "Juncos"},
        ],
    },
    {
        "scenario": "{quantity:{$lt:20}}",
        "expected": [{"name": "quantity", "value": "$lt:20"}],
    },
    {
        "scenario": "{ $or: [{ quantity: { $lt: 20 }}, { price: { $lt: 10 }}] }",
        "expected": [{"name": "$or", "value": "{quantity:{$lt:20}},{price:{$lt:10}}"}],
    },
    {
        "scenario": "{ $and: [ { quantity: { $lt: 20 }}, { price: { $lt: 10 }}] }",
        "expected": [{"name": "$and", "value": "{quantity:{$lt:20}},{price:{$lt:10}}"}],
    },
    {
        "scenario": " { qty: { $in: [ 5, 15 ] } }",
        "expected": [{"name": "qty", "value": "$in:[5,15]"}],
    },
    {
        "scenario": '{ center : { $eq : "Came"}, homepage_featured : { $ne : 0}}',
        "expected": [
            {"name": "center", "value": '$eq:"Came"'},
            {"name": "homepage_featured", "value": "$ne:0"},
        ],
    },
]


@pytest.mark.parametrize("case", use_cases)
def test_wheres(case):
    container = WheresContainer()
    command = container.wheres_service()
    response = command.execute(case["scenario"])
    assert response == case["expected"]
