# Blackjack game

# prints title
print ('''
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       
       BLACKJACK
       
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       ''')
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

start = None
while(start != "y"):
    start = input("Please enter \"y\" to start the game: ")