

import random

class DurakGame:
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.computer_hand = []

    def initialize_game(self):
        self.deck = self.create_deck()
        random.shuffle(self.deck)
        self.player_hand = self.deck[:6]
        self.computer_hand = self.deck[6:12]

    def create_deck(self):
        ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['♠', '♣', '♥', '♦']
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(rank + suit)
        return deck

    def player_turn(self):
        print("Ваши карты:", self.player_hand)
        card_index = int(input("Выберите индекс карты для хода: "))
        card = self.player_hand.pop(card_index)
        print("Вы сыграли карту:", card)

    def computer_turn(self):
        card_index = random.randint(0, len(self.computer_hand) - 1)
        card = self.computer_hand.pop(card_index)
        print("Компьютер сыграл карту:", card)

game = DurakGame()
game.initialize_game()
game.player_turn()
game.computer_turn()
