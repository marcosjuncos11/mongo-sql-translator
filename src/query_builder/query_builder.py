from typing import List

from src.commands.conditions.iconditions import IConditions
from src.commands.select.iselect import ISelect
from src.commands.sql_builder.isql_builder import ISQLBuilder
from src.commands.wheres.iwheres import IWheres
from src.itranslator import ITranslator


class QueryBuilder(ITranslator):
    def __init__(
        self,
        conditions_command: IConditions,
        select_command: ISelect,
        wheres_command: IWheres,
        sql_builder_command: ISQLBuilder,
    ) -> None:
        self.conditions_command = conditions_command
        self.select_command = select_command
        self.wheres_command = wheres_command
        self.sql_builder_command = sql_builder_command

    def execute(
        self, dto_select_fields: List[str], dto_where_fields: str, table_name: str
    ) -> str:
        select_fields = self.select_command.execute(dto_select_fields)
        wheres_fields = self.wheres_command.execute(dto_where_fields)
        conditions = self.conditions_command.execute(wheres_fields)

        return self.sql_builder_command.execute(select_fields, table_name, conditions)
