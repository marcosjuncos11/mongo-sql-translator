import pytest
from unittest.mock import Mock
from src.query_builder.query_builder import QueryBuilder

def test_query_builder():
    conditions_command_mock = Mock()
    conditions_command_mock.execute.return_value = []
    select_command = Mock()
    select_command.execute.return_value = []
    wheres_command = Mock()
    wheres_command.execute.return_value = []
    sql_builder_command = Mock()
    sql_builder_command.execute.return_value = "select * from users;"
    cmd = QueryBuilder(conditions_command_mock, select_command, wheres_command, sql_builder_command)    
    response = cmd.execute([], "wheres", "table")
    
    
    conditions_command_mock.execute.assert_called_once()
    select_command.execute.assert_called_once()
    wheres_command.execute.assert_called_once()
    sql_builder_command.execute.assert_called_once()    
    assert response == "select * from users;"
    