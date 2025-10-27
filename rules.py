
class Rules:

    @staticmethod
    def valid_value(value : str) -> bool:
        '''Check if the value given is valid'''
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        return value in values
    
    @staticmethod
    def hand_comparison(hand1, hand2, cards):

