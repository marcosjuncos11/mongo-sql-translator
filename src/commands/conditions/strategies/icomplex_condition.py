from abc import ABC, abstractmethod


class IComplexCondition(ABC):
    @abstractmethod
    def execute():
        pass
