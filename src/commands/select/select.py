from src.commands.select.iselect import ISelect


class Select(ISelect):
    def execute(self, query: str) -> dict:
        """Parses the mongodb query and gets field names to be query

        Args:
            query (str): mongo db query

        Returns:
            dict: returns fields to be query
        """
        try:
            if query == "":
                return ["*"]
            inside = query[query.find("{") + 1 : query.find("}")]
            fields = inside.split(",")
            select_fields = [field.split(":")[0] for field in fields]
            return select_fields
        except Exception as e:
            print(e)
            raise e
