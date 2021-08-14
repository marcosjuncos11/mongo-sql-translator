"""
Chain of responsability pattern
"""
from src.itranslator import ITranslator
from src.commands.table.itable import ITable

class Translator(ITranslator):
  def __init__(self, table: ITable) -> None:
    self.table = table
      
  def execute(self, query: str) -> str:
    dto = None
    
    dto = self.table.execute(query)
    
    return dto