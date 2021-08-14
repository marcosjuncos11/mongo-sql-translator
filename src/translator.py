"""
Chain of responsability pattern
"""
from src.itranslator import ITranslator
from src.commands.table.itable import ITable
from src.commands.select.iselect import ISelect
from src.commands.wheres.iwheres import IWheres
from src.commands.mongo_find_params.imongo_find_params import IMongoFindParams

class Translator(ITranslator):
  def __init__(self, table_command: ITable, mongo_find_params_command: IMongoFindParams, select_command: ISelect, wheres_command: IWheres) -> None:
    self.table_command = table_command
      
  def execute(self, query: str) -> str:
    dto = None
    
    dto = self.table_command.execute(query)
    
    table_name = dto["table_name"]
    
    dto = self.mongo_find_params_command.execute(dto["processed_query"])
    
    select_fields = self.select_command.execute(dto["select_fields"])    
    wheres_fields = self.wheres_command.execute(dto["where_fields"])    
        
    return dto