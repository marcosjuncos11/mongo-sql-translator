from typing import List
from src.commands.validator.iquery_type_validator import IQueryTypeValidator


class QueryTypeValidator(IQueryTypeValidator):
    supported = 'find('
    def execute(self, query: str) -> None:
        """verify if type of query is accepted

        Args:
            query (str): mongodb query

        """
        query_split: List[str] = query.split(".")
        if not query_split[2].startswith(self.supported):
            raise Exception("Unsupported mongo operations")
        