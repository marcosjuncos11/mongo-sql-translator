from abc import ABC, abstractmethod

class ISimple(ABC):
  @abstractmethod
  def execute():
    pass
  