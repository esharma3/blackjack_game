# importing dependencies
import os
import random

# creating class for card values and suit
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        return

    def __repr__(self):
        return f"{self.value} of {self.suit}"


# creating class for building the deck (inheriting from Card class), shuffling the deck and drawing a card
class Deck(Card):
    def __init__(self):
        super().__init__(value, suit)
        self.cards = []
        self.deck = []
        self.card = ""
        return

    def deck_of_cards(self):
        for s in range(0, 4):
            for v in range(0, 13):
                self.card = self.value[v] + " of " + self.suit[s]
                self.deck.append(self.card)
        return

    def __repr__(self):
        return f"{self.deck}"

    def shuffle(self):
        random.shuffle(self.deck)
        return

    def draw(self):
        return self.deck.pop()


# creating class for player hand and player total score (inheriting from Deck class)
class Player(Deck):
    def __init__(self):
        super().__init__()
        self.hand = []
        self.sum = 0
        self.non_aces = ""
        self.aces = ""
        return

    def add_card(self, deck):
        self.hand.append(deck.draw())
        return

    def __repr__(self):
        return f'Player Cards: [{"][".join(self.hand)}] ({self.sum})'

    def score(self):
        self.sum = 0
        self.non_aces = [card[:2] for card in self.hand if card[:1] != "A"]
        self.aces = [card[:2] for card in self.hand if card[:1] == "A"]

        for card in self.non_aces:
            card = card.strip()
            if card in "JQK":
                self.sum += 10
            else:
                self.sum += int(card)

        for card in self.aces:
            if self.sum <= 10:
                self.sum += 11
            else:
                self.sum += 1
        return self.sum


# creating class for dealer hand and dealer total score (inheriting from Player and Deck class)
class Dealer(Player, Deck):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'Dealer Cards: [{"][".join(self.hand)}] ({self.sum})'


# creating class for playing the game of Blackjack (includes functions for hit and stand)
class Play:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.deck.deck_of_cards()
        self.deck.shuffle()
        self.first_hand = True
        self.standing = False
        self.p_score = 0
        self.d_score = 0
        self.choice = ""
        # print(self.deck)
        return

    def play_blackjack(self):

        self.player.add_card(self.deck)
        self.dealer.add_card(self.deck)
        self.player.add_card(self.deck)
        self.dealer.add_card(self.deck)

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            self.p_score = self.player.score()
            self.d_score = self.dealer.score()

            if self.standing:
                print(self.dealer)
            else:
                print(f"Dealer Cards: [{self.dealer.hand[0]}][?]")

            print(self.player)
            print("")

            if self.standing:
                if self.d_score > 21:
                    print("Dealer busted, you win!")
                elif self.p_score == self.d_score:
                    print("Tie!! Nobody Wins or Loses!")
                elif self.p_score > self.d_score:
                    print("You beat the dealer, you win!")
                else:
                    print("You lose!!")
                break

            if self.first_hand and self.p_score == 21:
                print("BlackJack! Game Over!")
                break

            self.first_hand = False

            if self.p_score > 21:
                print("You busted!")
                break

            print("What would you like to do?")
            print(" [1] Hit")
            print(" [2] Stand")
            print("")

            self.choice = input("Your choice: ")
            print("")

            if self.choice == "1":
                self.hit()
            elif self.choice == "2":
                self.stand()
        return

    def hit(self):
        self.player.add_card(self.deck)
        return

    def stand(self):
        self.standing = True
        while self.dealer.score() <= 16:
            self.dealer.add_card(self.deck)
        return


# main script

value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

play = Play()
play.play_blackjack()