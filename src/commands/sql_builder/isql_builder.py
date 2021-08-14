from abc import ABC, abstractmethod


class ISQLBuilder(ABC):
    @abstractmethod
    def execute():
        pass
