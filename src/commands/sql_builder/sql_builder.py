from src.commands.sql_builder.isql_builder import ISQLBuilder


class SQLBuilder(ISQLBuilder):
    def execute(self, select: str, table: str, conditions: str) -> dict:
        try:
            return f"SELECT {select} FROM {table} WHERE {conditions};"
        except Exception as e:
            print(e)
            raise e
