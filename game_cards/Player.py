import random


class Player:
    def __init__(self, name, num_of_cards=10):
        self.name = name
        if num_of_cards > 26:
            self.num_of_cards = 26
        else:
            self.num_of_cards = num_of_cards
        self.__hand = []

    def set_hand(self, deck):
        """get a deck and give the player new cards for the hand"""
        for i in range(self.num_of_cards):
            self.__hand.append(deck.deal_one())

    def __str__(self):
        return f"name: {self.name}, hand: {self.__hand}"

    def __repr__(self):
        return f"name: {self.name}, hand: {self.__hand}"

    def get_card(self):
        """take a random card from the player"""
        return self.__hand.pop(random.randint(0, len(self.__hand) - 1))

    def add_card(self, card):
        """gets a card and add it to the player hand"""
        self.__hand.append(card)

    def show(self):
        """prints the player name and hand"""
        print(f"name: {self.name}, hand: {self.__hand}")

    def get_hand(self):
        return len(self.__hand)
