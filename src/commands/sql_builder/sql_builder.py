from typing import List
from src.commands.sql_builder.isql_builder import ISQLBuilder


class SQLBuilder(ISQLBuilder):
    def execute(self, select_fields: List[str], table: str, conditions: str) -> str:
        """creates SQL (string)

        Args:
            select (str): fields
            table (str): table name
            conditions (str): wheres clausule

        Returns:
            str: final sql query string
        """
        try:
            select = ",".join(select_fields)
            return f"SELECT {select} FROM {table} WHERE {conditions};"
        except Exception as e:
            print(e)
            raise e
