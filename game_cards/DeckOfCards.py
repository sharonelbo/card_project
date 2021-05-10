from game_cards.Card import Card
from random import randint, shuffle


class DeckOfCards(Card):
    def __init__(self):
        """creates a deck with 52 cards"""
        self.deck = []
        for n in range(1, 14):
            card1 = Card(n, "diamond")
            self.deck.append(card1)

        for n in range(1, 14):
            card1 = Card(n, "spade")
            self.deck.append(card1)

        for n in range(1, 14):
            card1 = Card(n, "heart")
            self.deck.append(card1)

        for n in range(1, 14):
            card1 = Card(n, "club")
            self.deck.append(card1)

    def shuffle(self):
        """shuffles the deck"""
        shuffle(self.deck)

    def __repr__(self):
        """returns a string when printing"""
        return f"{self.deck}"

    def __str__(self):
        """returns a string when printing"""
        return f"{self.deck}"

    def deal_one(self):
        """draws one random card from the deck and returns it"""
        return self.deck.pop(randint(0, len(self.deck) - 1))

    def show(self):
        """print the deck"""
        print(self.deck)
