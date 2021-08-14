from typing import List
from src.commands.wheres.iwheres import IWheres
from src.commands.wheres.operators_processors.isimple import ISimple
from src.commands.wheres.operators_processors.icomplex import IComplex
class Wheres(IWheres):
    
  def __init__(self, simple_operator_processor: ISimple, complex_operator_processor: IComplex) -> None:
    self.simple_operator_processor = simple_operator_processor
    self.complex_operator_processor = complex_operator_processor
      
    
  def execute(self, query: str) -> dict:
    try:  
      # remove openings 
      query = query.strip()
      query = query[1:-1]
      # split operations
      results = self.complex_operator_processor.execute(query)
      # print("results", results)
      if len(results) == 0:
        results = self.simple_operator_processor.execute(query)
        # print("results2", results)
      return results
    except Exception as e:
      print(e)
      raise e
    
