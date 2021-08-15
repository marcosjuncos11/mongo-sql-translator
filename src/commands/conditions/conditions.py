from src.commands.conditions.iconditions import IConditions
from src.commands.conditions.strategies.icomplex_condition import \
    IComplexCondition
from src.commands.conditions.strategies.isimple_condition import \
    ISimpleCondition


class Conditions(IConditions):
    def __init__(
        self, complex_strategy: IComplexCondition, simple_strategy: ISimpleCondition
    ) -> None:
        self.complex_strategy = complex_strategy
        self.simple_strategy = simple_strategy

    def execute(self, conditions: str) -> dict:
        try:
            sql = ""
            for condition in conditions:
                strategy = (
                    self.complex_strategy
                    if condition["name"] in self.complex_strategy.operations
                    else self.simple_strategy
                )
                sql += " AND " if sql != "" else ""
                sql += strategy.execute(condition)
            return sql
        except Exception as e:
            print(e)
            raise e
