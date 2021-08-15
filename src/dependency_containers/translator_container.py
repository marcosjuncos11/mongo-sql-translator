from dependency_injector import containers, providers
from src.translator import Translator
from src.commands.table.table import Table
from src.dependency_containers.conditions_container import ConditionsContainer
from src.commands.mongo_find_params.mongo_find_params import MongoFindParams
from src.commands.select.select import Select
from src.commands.sql_builder.sql_builder import SQLBuilder
from src.commands.validator.query_type_validator import QueryTypeValidator
from src.dependency_containers.wheres_container import WheresContainer


class TranslatorContainer(containers.DeclarativeContainer):
    query_type_validator = providers.Factory(QueryTypeValidator)
    sql_builder_command = providers.Factory(SQLBuilder)
    table_command = providers.Factory(Table)
    mongo_find_params_command = providers.Factory(MongoFindParams)
    select_command = providers.Factory(Select)
    container = ConditionsContainer()
    conditions_command = container.conditions_service()
    container = WheresContainer()
    wheres_command = container.wheres_service()
    translator_service = providers.Factory(
        Translator,
        table_command,
        conditions_command,
        mongo_find_params_command,
        select_command,
        wheres_command,
        sql_builder_command,
        query_type_validator,
    )
