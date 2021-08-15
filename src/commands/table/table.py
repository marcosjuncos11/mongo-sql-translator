from typing import List
from src.commands.table.itable import ITable


class Table(ITable):
    def execute(self, query: str) -> dict:
        """processes mongo db query to get sql table name

        Args:
            query (str): mongodb query

        Returns:
            dict: table name and the rest of the query
        """
        try:
            query_split: List[str] = query.split(".")
            return {
                "table": query_split[1],
                "processed_query": query_split[2],
            }
        except Exception as e:
            print(e)
            raise e
