class Card:
    def __init__(self, suit, value):
        """creates a card that has a suit and a value"""
        if type(value) == int:
            if 0<=value<=13:
                self.value = value
        else:
            self.value = None
            return "Error"

        if suit != "diamond" and suit != "spade" and suit != "heart" and suit != "club":
            self.suit = None
        else:
            self.suit = suit

        if self.suit == "diamond":
            self.__power = 1
        elif self.suit == "spade":
            self.__power = 2
        elif self.suit == "heart":
            self.__power = 3
        elif self.suit == "club":
            self.__power = 4
        elif self.suit == None:
            self.__power = 0

    def __str__(self):
        """"""
        return f"{self.value} {self.suit}"

    def __eq__(self, other):
        """return True if two cards are equal and False if not"""
        if self.value == other.value and self.__power == other.__power:
            return True
        else:
            return False

    def __gt__(self, other):
        """return True if a card is greater than the other and False if not"""
        if self.value == 1 and other.value > 1:
            return True
        if self.value > 1 and other.value == 1:
            return False
        if self.value > other.value:
            return True
        elif self.value < other.value:
            return False
        else:
            if self.__power > other.__power:
                return True
            else:
                return False

    def __repr__(self):
        return f"{self.value} {self.suit}"