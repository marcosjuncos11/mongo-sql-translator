import pytest
from src.commands.mongo_find_params.mongo_find_params import MongoFindParams

use_cases = [
    {
        "scenario": "find({name:'julio'});",
        "select_fields": "",
        "where_fields": "{name:'julio'}",
    },
    {
        "scenario": "find({_id:23113},{name:1,age:1});",
        "select_fields": "{name:1,age:1}",
        "where_fields": "{_id:23113}",
    },
    {
        "scenario": "find({_id:23113},{lastname:1,age:1});",
        "select_fields": "{lastname:1,age:1}",
        "where_fields": "{_id:23113}",
    },
    {
        "scenario": 'find({ "center_id" : { "$eq" : 55}, "homepage_featured" : { "$ne" : 0}},{firstname:1});',
        "select_fields": "{firstname:1}",
        "where_fields": '{ "center_id" : { "$eq" : 55}, "homepage_featured" : { "$ne" : 0}}',
    },
]


@pytest.mark.parametrize("case", use_cases)
def test_mongo_find_param(case):
    command = MongoFindParams()
    response = command.execute(case["scenario"])
    assert response["select_fields"] == case["select_fields"]
    assert response["where_fields"] == case["where_fields"]
