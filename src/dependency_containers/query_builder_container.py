from dependency_injector import containers, providers

from src.commands.select.select import Select
from src.commands.sql_builder.sql_builder import SQLBuilder
from src.dependency_containers.conditions_container import ConditionsContainer
from src.dependency_containers.wheres_container import WheresContainer
from src.query_builder.query_builder import QueryBuilder


class QueryBuilderContainer(containers.DeclarativeContainer):
    sql_builder_command = providers.Factory(SQLBuilder)
    select_command = providers.Factory(Select)
    container = ConditionsContainer()
    conditions_command = container.conditions_service()
    container = WheresContainer()
    wheres_command = container.wheres_service()
    query_builder_service = providers.Factory(
        QueryBuilder,
        conditions_command,
        select_command,
        wheres_command,
        sql_builder_command,
    )
