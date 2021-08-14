from dependency_injector import containers, providers
from src.translator import Translator
from src.commands.table.table import Table



class TranslatorContainer(containers.DeclarativeContainer):
    table_command = providers.Factory(Table)
    translator_service = providers.Factory(
        Translator,
        table_command,
    )


    