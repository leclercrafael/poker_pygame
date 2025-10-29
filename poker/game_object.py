import abc


import typing 

class GameObject(abc.ABC) :
    """The goal of this class is to define some methods that every GameObject's class
    needs to contain"""

    def __init__(self) -> None :
        """Object initialization"""
        super().__init__() 

        pass


    @abc.abstractmethod
    def draw(self) -> None: 
        """Draw the object"""
        raise NotImplementedError

    def is_background(self) -> bool:
        """Tell if this object is a background object."""
        return False



