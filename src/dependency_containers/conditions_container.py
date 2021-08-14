from dependency_injector import containers, providers
from src.commands.conditions.conditions import Conditions
from src.dependency_containers.complex_strategy_container import (
    ComplexStrategyContainer,
)
from src.commands.conditions.strategies.simple_condition import SimpleCondition


class ConditionsContainer(containers.DeclarativeContainer):
    container = ComplexStrategyContainer()
    complex_strategy = container.complex_condition_service()
    simple_strategy = providers.Factory(SimpleCondition)
    conditions_service = providers.Factory(
        Conditions,
        complex_strategy,
        simple_strategy,
    )
