class Pot() :

    def __init__(self,value : int) -> None :
        """Initialize the variables""" 
        self._value = value
        

    def __add__(self,_raise : int ) -> None :
        """Add the raises to the pot"""
        self._value += _raise

    @property
    def value(self) -> int :
        """Return the value of the pot""" 
        return(self._value)
    
    @value.setter
    def value(self,Value : int) -> None :
        """Value of the Pot"""
        self._value = Value

    


    


