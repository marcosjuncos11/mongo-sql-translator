from abc import ABC, abstractmethod


class IQueryTypeValidator(ABC):
    @abstractmethod
    def execute():
        pass
