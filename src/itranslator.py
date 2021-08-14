from abc import ABC, abstractmethod


class ITranslator(ABC):
    @abstractmethod
    def execute():
        pass
