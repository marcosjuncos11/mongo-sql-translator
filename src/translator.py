from src.commands.conditions.iconditions import IConditions
from src.commands.mongo_find_params.imongo_find_params import IMongoFindParams
from src.commands.select.iselect import ISelect
from src.commands.table.itable import ITable
from src.commands.validator.iquery_type_validator import IQueryTypeValidator
from src.commands.wheres.iwheres import IWheres
from src.itranslator import ITranslator
from src.query_builder.iquery_builder import IQueryBuilder


class Translator(ITranslator):
    def __init__(
        self,
        table_command: ITable,
        mongo_find_params_command: IMongoFindParams,
        query_builder_command: IQueryBuilder,
        query_type_validator: IQueryTypeValidator,
    ) -> None:
        self.table_command = table_command
        self.mongo_find_params_command = mongo_find_params_command
        self.query_type_validator = query_type_validator
        self.query_builder_command = query_builder_command

    def execute(self, query: str) -> str:

        self.query_type_validator.execute(query)
        dto = self.table_command.execute(query)

        table_name = dto["table"]
        dto = self.mongo_find_params_command.execute(dto["processed_query"])

        sql = self.query_builder_command.execute(
            dto["select_fields"], dto["where_fields"], table_name
        )

        return sql
