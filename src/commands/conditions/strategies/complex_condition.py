from src.commands.conditions.strategies.icomplex_condition import IComplexCondition
from src.commands.conditions.strategies.isimple_condition import ISimpleCondition
from src.commands.wheres.iwheres import IWheres

class ComplexCondition(IComplexCondition):
  
  operations = ["$and", "$or"]  
  operations_mapping = {"$and": " AND ", "$or": " OR "}  
  
  def __init__(self, wheres_command: IWheres, simple_condition_strategy: ISimpleCondition) -> None:
      self.wheres_command = wheres_command
      self.simple_condition_strategy = simple_condition_strategy
  
  def execute(self, condition: str) -> dict:
    try:
      sql = " ("
      operator = self.operations_mapping.get(condition["name"])
      simple_conditions = self._split_conditions(condition["value"])
      sql += self._get_sql(simple_conditions, operator)
      sql += ") "      
      return sql
        
    except Exception as e:
      print(e)
      raise e
    
  def _get_sql(self, simple_conditions, operator: str):
    sql = ""
    for simple_condition in simple_conditions:
      where = self.wheres_command.execute(simple_condition)
      operation = self.simple_condition_strategy.execute(where[0])
      sql += f"{operator}" if sql != "" else ""
      sql += f"{operation}"
    return sql
  
  def _split_conditions(self, condition: str):    
    r = []
    res = self._get_parameter(condition.strip())
    if res == "":
      return r
    r.append(res)    
    if len(res) < len(condition.strip()):
      new_str = condition.replace(res, "")
      r = r + self._split_conditions(new_str.strip())          
    return r
    
  def _get_parameter(self, query: str):
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