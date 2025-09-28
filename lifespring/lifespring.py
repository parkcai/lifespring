from .external import *


__all__ = [
    "lifespring",
]



class LifeSpring:
    
    def __init__(
        self,
        database_path: str,
    )-> None:
        
        self._database_path = database_path


lifespring = LifeSpring(
    database_path = "data"
)