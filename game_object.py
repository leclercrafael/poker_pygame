import abc
from .pix import Pix

import typing 

class GameObject(abc.ABC,Pix) :
    """The goal of this class is to define some methods that every GameObject's class
    need to contain"""

    def __init__(self) -> None :
        """Object initialization"""

        
        pass

    @property
    @abc.abstractmethod
    def draw(self) -> typing.Iterator[Pix]: 
        """Draw the object"""
        raise NotImplementedError

    def is_background(self) -> bool:
        """Tell if this object is a background object."""
        return False



