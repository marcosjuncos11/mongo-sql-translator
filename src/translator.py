"""
Chain of responsability pattern
"""
from src.itranslator import ITranslator
from src.commands.table.itable import ITable
from src.commands.select.iselect import ISelect
from src.commands.wheres.iwheres import IWheres
from src.commands.sql_builder.isql_builder import ISQLBuilder
from src.commands.mongo_find_params.imongo_find_params import IMongoFindParams
from src.commands.conditions.iconditions import IConditions

class Translator(ITranslator):
  def __init__(self, table_command: ITable, conditions_command: IConditions, mongo_find_params_command: IMongoFindParams, select_command: ISelect, wheres_command: IWheres, sql_builder_command: ISQLBuilder) -> None:
    self.table_command = table_command
    self.conditions_command = conditions_command
    self.mongo_find_params_command = mongo_find_params_command
    self.select_command = select_command
    self.wheres_command = wheres_command
    self.sql_builder_command = sql_builder_command
      
  def execute(self, query: str) -> str:
    dto = None
    
    dto = self.table_command.execute(query)
    
    print("table", dto)
    table_name = dto["table"]
    dto = self.mongo_find_params_command.execute(dto["processed_query"])
    
    select_fields = self.select_command.execute(dto["select_fields"]) 
    print("select_fields", select_fields)
    wheres_fields = self.wheres_command.execute(dto["where_fields"])    
    print("wheres_fields", wheres_fields)
    conditions = self.conditions_command.execute(wheres_fields)    
    print("conditions", conditions)
    
    select = ",".join(select_fields)
    sql = self.sql_builder_command.execute(select, table_name, conditions)
    print("sql")
    print(sql)
    return sql