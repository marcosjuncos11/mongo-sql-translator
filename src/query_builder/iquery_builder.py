from abc import ABC, abstractmethod


class IQueryBuilder(ABC):
    @abstractmethod
    def execute():
        pass
