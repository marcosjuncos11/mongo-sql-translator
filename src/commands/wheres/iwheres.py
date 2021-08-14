from abc import ABC, abstractmethod


class IWheres(ABC):
    @abstractmethod
    def execute():
        pass
