# Blackjack game

import random 


# prints title
print ('''
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       
       BLACKJACK
       
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       ''')

# prints rules
print ('''
       Rules:
       1. The dealer will deal the player two cards.
       2. The total value is the sum of the value of each card. Face cards count as 10
          and aces count as either a 1 or an 11.
       3. The goal of the game is to reach a value of 21. If the value exceeds 21, it is a bust.
       4. They player may choose to hit or stand. If the player hits, the player recieves another card.
          If the player stands, the player will not recieve any more cards.
       5. After the player's turn, the dealer will play their cards.
       6. The winner is decided by who has the higher total amount or the person that did not bust.
       ''')

possible_cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
dealt_cards_player = []
dealt_cards_dealer = []
# function that deals cards
def deal_cards(cards):
       for i in range(2):
              cards.append(random.randint(0, 12))
       
def dealt_ace_11(card):
       card = 11

def dealt_ace_1(card):
       card = 1
              
def count_total():
       pass

# starts the game when player enters y
start = None
while(start != "y"):
       start = input("Please enter \"y\" to start the game: ")
       
deal_cards(dealt_cards_player)

   