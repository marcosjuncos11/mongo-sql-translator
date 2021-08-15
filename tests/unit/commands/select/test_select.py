import pytest

from src.commands.select.select import Select

use_cases = [
    {"scenario": "", "select_fields": ["*"]},
    {
        "scenario": "{lastname:1}",
        "select_fields": ["lastname"],
    },
    {
        "scenario": "{name:1,age:1}",
        "select_fields": ["name", "age"],
    },
]


@pytest.mark.parametrize("case", use_cases)
def test_select(case):
    table_command = Select()
    response = table_command.execute(case["scenario"])
    assert response == case["select_fields"]
