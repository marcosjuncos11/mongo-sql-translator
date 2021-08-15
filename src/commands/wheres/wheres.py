from typing import List
from src.commands.wheres.iwheres import IWheres
from src.commands.wheres.operators_processors.isimple import ISimple
from src.commands.wheres.operators_processors.icomplex import IComplex


class Wheres(IWheres):
    def __init__(
        self, simple_operator_processor: ISimple, complex_operator_processor: IComplex
    ) -> None:
        self.simple_operator_processor = simple_operator_processor
        self.complex_operator_processor = complex_operator_processor

    def execute(self, query: str) -> dict:
        """Processes the conditions and group according different operators parsing them to SQL's one

        Args:
            query (str): pre-processed query

        Returns:
            dict: contains sql condition format
        """
        try:
            # remove openings
            query: str = query.strip()
            query: str = query[1:-1]
            # split operations
            results: str = self.complex_operator_processor.execute(query)
            if len(results) == 0:
                results = self.simple_operator_processor.execute(query)
            return results
        except Exception as e:
            print(e)
            raise e
