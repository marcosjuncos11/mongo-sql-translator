from dependency_injector import containers, providers
from src.commands.wheres.operators_processors.simple import Simple
from src.commands.wheres.operators_processors.complex import Complex
from src.commands.wheres.wheres import Wheres


class WheresContainer(containers.DeclarativeContainer):
    simple = providers.Factory(Simple)
    complex = providers.Factory(Complex)
    wheres_service = providers.Factory(
        Wheres,
        simple,
        complex,
    )
