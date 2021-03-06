class Card:
    def __init__(self, value, suit):
        """creates a card that has a suit and a value"""
        if type(value) == int:
            if 1 <= value <= 13:
                self.value = value
            else:
                self.value = None
        else:
            self.value = None

        if suit != "diamond" and suit != "spade" and suit != "heart" and suit != "club":
            self.suit = None
        else:
            self.suit = suit

        if self.suit is None:
            self.__power = 0
            self.__symbol = None
        elif self.suit == "diamond":
            self.__power = 1
            self.__symbol = "♦"
        elif self.suit == "spade":
            self.__power = 2
            self.__symbol = "♠"
        elif self.suit == "heart":
            self.__power = 3
            self.__symbol = "♥"
        elif self.suit == "club":
            self.__power = 4
            self.__symbol = "♣"


    def __str__(self):
        """returns a string when printing"""
        return f"{self.value}{self.__symbol}"

    def __gt__(self, other):
        """return True if a card is greater than the other and False if not"""
        if self.value is not None and self.__power != 0 and other.value is not None and other.__power != 0:
            if self.value == 1 and other.value > 1:
                return True
            if self.value > 1 and other.value == 1:
                return False
            if self.value > other.value:
                return True
            if self.value < other.value:
                return False
            else:
                if self.__power > other.__power:
                    return True
                else:
                    return False
        else:
            print("Error one card or more isn't valid")

    def __repr__(self):
        """returns a string when printing"""
        return f"{self.value}{self.__symbol}"

    def __eq__(self, other):
        """return True if two cards are equal and False if not"""
        if self.value is not None and self.__power != 0 and other.value is not None and other.__power != 0:
            if self.value == other.value and self.__power == other.__power:
                return True
            else:
                return False
        else:
            print("Error one card or more isn't valid")

