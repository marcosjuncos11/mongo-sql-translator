from typing import List
from src.commands.wheres.operators_processors.icomplex import IComplex

class Complex(IComplex):
  operators = ["$or", "$and"]
  def execute(self, query: str) -> List[dict]:
    stack = []
    chain, openings, closings, name, open_symbol, close_symbol = self._ini_vars()
    for s in query:
      if s in " ":
        continue
      if s == ":" and openings == 0:
        name = chain
        if name in self.operators:
          open_symbol = "["
          close_symbol = "]"  
        chain = ""
        continue
      if s == open_symbol:
        openings += 1
        continue
      if s == close_symbol:
        closings += 1
      if s == close_symbol and openings == closings:
        name = name[1:] if name[0] == "," else name
        # print(chain.find("*"), type(chain))
        # if chain.find("{") != -1 and chain.find("}") != -1:
        #   print("chain1", chain)        
        #   chain = chain.strip()
        #   chain = chain[1:-1]
        #   print("name", name)
        #   print("chain", chain)        
        #   new_value = self.execute(chain)
        #   print("new_valuen", new_value)
        stack.append({"name": name, "value": chain})
        chain, openings, closings, name, open_symbol, close_symbol = self._ini_vars()
        continue                
      chain += s        
    
    return stack
  
  def _ini_vars(self):
    return "", 0, 0, None, "{", "}"