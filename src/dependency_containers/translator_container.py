from dependency_injector import containers, providers

from src.commands.mongo_find_params.mongo_find_params import MongoFindParams
from src.commands.table.table import Table
from src.commands.validator.query_type_validator import QueryTypeValidator
from src.dependency_containers.query_builder_container import \
    QueryBuilderContainer
from src.translator import Translator


class TranslatorContainer(containers.DeclarativeContainer):
    query_type_validator = providers.Factory(QueryTypeValidator)
    table_command = providers.Factory(Table)
    mongo_find_params_command = providers.Factory(MongoFindParams)
    container = QueryBuilderContainer()
    query_builder_command = container.query_builder_service()
    translator_service = providers.Factory(
        Translator,
        table_command,
        mongo_find_params_command,
        query_builder_command,
        query_type_validator,
    )
