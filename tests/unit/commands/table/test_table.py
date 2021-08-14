import pytest
from src.commands.table.table import Table

use_cases = [
    {
        "scenario": "db.user.find({name:'julio'});",
        "table_name": "user",
        "processed_query": "find({name:'julio'});",
    },
    {
        "scenario": "db.user.find({_id:23113},{name:1,age:1});",
        "table_name": "user",
        "processed_query": "find({_id:23113},{name:1,age:1});",
    },
    {
        "scenario": "db.person.find({_id:23113},{name:1,age:1});",
        "table_name": "person",
        "processed_query": "find({_id:23113},{name:1,age:1});",
    },
]


@pytest.mark.parametrize("case", use_cases)
def test_table(case):
    table_command = Table()
    response = table_command.execute(case["scenario"])
    assert response["table"] == case["table_name"]
    assert response["processed_query"] == case["processed_query"]
