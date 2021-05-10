import random
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card


class Player:
    def __init__(self, name, num_of_cards=10):
        if type(name) == str:
            self.name = name
        else:
            self.name = "player"
        if type(num_of_cards) == int:
            if num_of_cards > 26:
                self.num_of_cards = 26
            elif num_of_cards < 0:
                self.num_of_cards = 0
            else:
                self.num_of_cards = num_of_cards
        else:
            self.num_of_cards = 10
        self.__hand = []

    def set_hand(self, deck):
        """get a deck and give the player new cards for the hand"""
        if type(deck) == DeckOfCards:
            for i in range(self.num_of_cards):
                self.__hand.append(deck.deal_one())
        else:
            print("Error you need to enter a valid deck")

    def __str__(self):
        """returns a string when printing"""
        return f"name: {self.name}, hand: {self.__hand}"

    def __repr__(self):
        """returns a string when printing"""
        return f"name: {self.name}, hand: {self.__hand}"

    def get_card(self):
        """take a random card from the player"""
        if len(self.__hand) > 0:
            return self.__hand.pop(random.randint(0, len(self.__hand) - 1))
        else:
            print("the player doesnt have cards in his hands")

    def add_card(self, card):
        """gets a card and add it to the player hand"""
        if type(card) == Card:
            self.__hand.append(card)
        else:
            print("Error you need to enter a valid card")

    def show(self):
        """prints the player name and hand"""
        print(f"name: {self.name}, hand: {self.__hand}")
