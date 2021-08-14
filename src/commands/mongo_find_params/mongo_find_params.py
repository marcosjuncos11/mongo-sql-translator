from src.commands.mongo_find_params.imongo_find_params import IMongoFindParams

class MongoFindParams(IMongoFindParams):
    
  def execute(self, query: str) -> dict:
    print(query)
    try:
      inside_parenthesis = query[query.find("(")+1:query.find(")")]
      where_fields = self._get_parameter(inside_parenthesis)      
      select_fields = self._get_parameter(inside_parenthesis[len(where_fields)+1:])
      print("select_fields", select_fields)
      print("where_fields", where_fields)
      return {
        "select_fields": select_fields,
        "where_fields": where_fields,
      }
    except Exception as e:
      print(e)
      raise e
    
  
  def _get_parameter(self, query: str):
    print("query", query)
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