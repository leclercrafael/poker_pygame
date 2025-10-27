from .game_object import GameObject

class Chip(GameObject):

    def __init__(self, value : float, color : str) -> None :
        super().__init__()
        self.value = value
        self.color = color

        

    