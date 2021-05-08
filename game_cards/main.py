from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from game_cards.CardGame import CardGame

player1 = input("please enter the first player name:")
player2 = input("please enter the second player name:")
game1 = CardGame(player1,player2,10)
game1.new_game()
print(game1)
for i in range(4):
    card1 = game1.players[0].get_card()
    card2 = game1.players[1].get_card()
    if card1 > card2:
        game1.players[1].add_card(card1)
        game1.players[1].add_card(card2)
        print(game1.players[0].name,"threw the card:",card1)
        print(game1.players[1].name, "threw the card:", card2)
        print("the winner of the round is:",game1.players[0].name)
    else:
        game1.players[0].add_card(card1)
        game1.players[0].add_card(card2)
        print(game1.players[0].name, "threw the card:", card1)
        print(game1.players[1].name, "threw the card:", card2)
        print("the winner of the round is:", game1.players[1].name)
print()
if game1.get_winner() != None:
    print("The winner of the game is",game1.get_winner().name)
else:
    print("Its a tie")




