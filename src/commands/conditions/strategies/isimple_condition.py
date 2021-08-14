from abc import ABC, abstractmethod

class ISimpleCondition(ABC):
  @abstractmethod
  def execute():
    pass
  