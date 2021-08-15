import pytest
from src.commands.validator.query_type_validator import QueryTypeValidator

use_cases = [
    {
        "scenario": "db.user.find({name:'julio'});",
    },
    {
        "scenario": "db.user.find({_id:23113},{name:1,age:1});",
    },
    {
        "scenario": "db.person.find({_id:23113},{name:1,age:1});",
    },
]


@pytest.mark.parametrize("case", use_cases)
def test_supported(case):
    command = QueryTypeValidator()
    command.execute(case["scenario"])
    assert True

unsupported_use_cases = [
    {
        "scenario": "db.user.findAll();",
    },
    {
        "scenario": "db.user.findOne({_id:23113},{name:1,age:1});",
    },
    {
        "scenario": "db.person.update({_id:23113},{name:1,age:1});",
    },
]


@pytest.mark.parametrize("case", unsupported_use_cases)
def test_unsupported(case):
    command = QueryTypeValidator()
    with pytest.raises(Exception):
        command.execute(case["scenario"])
    assert True
    
