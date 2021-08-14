from src.commands.table.itable import ITable


class Table(ITable):
    def execute(self, query: str) -> dict:
        try:
            query_split = query.split(".")
            return {
                "table": query_split[1],
                "processed_query": query_split[2],
            }
        except Exception as e:
            print(e)
            raise e
