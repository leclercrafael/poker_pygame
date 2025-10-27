class Combinaisons ():

    def __init__(self,flop : list, hand : list) -> None :
        self._flop = flop
        self._hand = hand

    def one_pair(self):
        p = 0
        for i in range (len(self._hand)):
            card = self._hand.pop()
            for j in range(len(self._hand)) :



            for card in self