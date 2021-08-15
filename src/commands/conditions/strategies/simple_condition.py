from src.commands.conditions.strategies.isimple_condition import ISimpleCondition


class SimpleCondition(ISimpleCondition):

    special_prefix_mapping = {
        "$eq:": "=",
        "$ne:": "!=",
        "$lt:": "<",
        "$lte:": "<=",
        "$gt:": ">",
        "$gte:": ">=",
        "$in:": " IN ",
    }

    special_fields = {"_id": "id"}

    special_prefix = ["$eq:", "$lt:", "$lte:", "$gt:", "$gte:", "$ne:", "$in:"]

    special_operators = ["$in:"]

    def execute(self, condition: str) -> dict:
        """Processes mongodb operators transforming them to SQL's

        Args:
            condition (str): mongodb format

        Returns:
            dict: sql's conditions
        """
        try:
            prefix_operator: str = self._prefix_operator(condition["value"])
            operator = "="
            value: str = condition["value"]
            add_str = True
            if prefix_operator != "" and prefix_operator in self.special_operators:
                add_str = False
                value = value.replace("[", "(")
                value = value.replace("]", ")")
            if prefix_operator != "":
                value = value.replace(prefix_operator, "")
                operator = self.special_prefix_mapping[prefix_operator]
            column_name = (
                self.special_fields[condition["name"]]
                if self.special_fields.get(condition["name"])
                else condition["name"]
            )
            value = f'"{value}"' if add_str else value
            sql: str = f" {column_name}{operator}{value}"
            return sql
        except Exception as e:
            print(e)
            raise e

    def _prefix_operator(self, value: str) -> str:
        for special_op in self.special_prefix_mapping:
            if value.startswith(special_op):
                return special_op

        return ""
