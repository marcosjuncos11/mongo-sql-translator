from abc import ABC, abstractmethod

class IConditions(ABC):
  @abstractmethod
  def execute():
    pass
  