from dependency_injector import containers, providers

from src.commands.conditions.strategies.complex_condition import \
    ComplexCondition
from src.commands.conditions.strategies.simple_condition import SimpleCondition
from src.dependency_containers.wheres_container import WheresContainer


class ComplexStrategyContainer(containers.DeclarativeContainer):
    simple = providers.Factory(SimpleCondition)
    container = WheresContainer()
    wheres = container.wheres_service()
    complex_condition_service = providers.Factory(
        ComplexCondition,
        wheres,
        simple,
    )
