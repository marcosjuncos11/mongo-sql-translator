from abc import ABC, abstractmethod

class IMongoFindParams(ABC):
  @abstractmethod
  def execute():
    pass
  