from src.commands.mongo_find_params.imongo_find_params import IMongoFindParams


class MongoFindParams(IMongoFindParams):
    def execute(self, query: str) -> dict:
        """split mongo query into select (fields) and wheres (conditions) sections

        Args:
            query (str): mongodb query

        Returns:
            dict: "select_fields": fields to be query
                  "where_fields": conditions to filtering
        """
        try:
            inside_parenthesis: str = query[query.find("(") + 1 : query.find(")")]
            where_fields: str = self._get_parameter(inside_parenthesis)
            select_fields: str = self._get_parameter(
                inside_parenthesis[len(where_fields) + 1 :]
            )
            return {
                "select_fields": select_fields,
                "where_fields": where_fields,
            }
        except Exception as e:
            print(e)
            raise e

    def _get_parameter(self, query: str) -> str:
        stack = ""
        openings = 0
        closings = 0
        for s in query:
            if s == "{":
                openings += 1
            if openings > 0:
                stack += s
            if s == "}":
                closings += 1
            if s == "}" and openings == closings:
                break

        return stack
