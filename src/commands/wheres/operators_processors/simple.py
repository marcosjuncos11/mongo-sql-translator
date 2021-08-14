from typing import List
from src.commands.wheres.operators_processors.isimple import ISimple

class Simple(ISimple):
  def execute(self, query: str) -> List[dict]:
    stack = []
    name = None
    chain = ""
    value = ""
    for s in query:
      if s in [" ", "\"", "'"]:
        continue
      if s == ":":
        name = chain
        chain = ""
        continue
      if s == ",":
        value = chain
        stack.append({"name": name, "value": chain})
        chain = ""
        name = ""
        continue
      chain += s
    stack.append({"name": name, "value": chain})  
    return stack