from abc import ABC, abstractmethod


class ITable(ABC):
    @abstractmethod
    def execute():
        pass
