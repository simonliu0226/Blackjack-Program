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

# lists all possible
possible_cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


# function that deals cards
def deal_card(cards):
       cards.append(possible_cards[random.randint(0, 12)])
       
       
# counts total value of the cards
def count_total(cards):
       total = 0
       for card in cards:
              if card == "A":
                     total += 11
                     if total > 21:
                            total -= 10
              elif (card == "J" or card == "Q" or card == "K"):
                     total += 10
              else:
                     total += card
       return total

# continues the game until the player decides to quit
play_again = None
while(play_again != "q"):
       dealt_cards_player = []
       dealt_cards_dealer = []
       hit_or_stand = None
       
# starts the game when player enters y
       start = None
       while(start != "y"):
              start = input("Please enter \"y\" to start the game: ")
       
# deals two cards to the player
       for i in range(2):
              deal_card(dealt_cards_player)
              deal_card(dealt_cards_dealer)
       print("You have been dealt a {card_1} and a {card_2}.".format(card_1=dealt_cards_player[0], card_2=dealt_cards_player[1]))
       print("Your current total is: {total}".format(total=count_total(dealt_cards_player)))
       
# checks to see if player wants to hit or stand
       while(True):
              if count_total(dealt_cards_player) < 21:
                     while(True):
                            hit_or_stand = input("Would you like to hit or stand? Enter \"h\" or \"s\": ")
                            if(hit_or_stand == "h") or (hit_or_stand == "s"):
                                   break
                     if hit_or_stand == "h":
                            deal_card(dealt_cards_player)
                            print("You have recieved a {card}.".format(card=dealt_cards_player[-1]))
                            print("Your new total is: {total}".format(total=count_total(dealt_cards_player)))
                     elif hit_or_stand == "s":
                            break
              elif count_total(dealt_cards_player) > 21:
                     print("You have bust. You lose.")
                     break
              else:
                     break

# the dealer draws cards, winning if they score higher than the player
       if count_total(dealt_cards_player) < 21:
              word = ""
              while count_total(dealt_cards_dealer) < 17:
                     deal_card(dealt_cards_dealer)
              if (count_total(dealt_cards_dealer) == 17) and ("A" in dealt_cards_dealer):
                     deal_card(dealt_cards_dealer)
              
# prints what the dealer drew and what their total is
              for card in dealt_cards_dealer:
                     word += " a " + str(card)
              print("The dealer draws" + word + ".")
              print("Their total is: {total}".format(total=count_total(dealt_cards_dealer)))
              
# prints whether player wins or loses              
              if count_total(dealt_cards_dealer) <= 21:      
                     if count_total(dealt_cards_player) > count_total(dealt_cards_dealer):
                            print("You have won with a score of {total_player} compared to the dealer's total of {total_dealer}.".format(total_player=count_total(dealt_cards_player),total_dealer=count_total(dealt_cards_dealer)))
                     elif count_total(dealt_cards_player) < count_total(dealt_cards_dealer):
                            print("You have lost with a score of {total_player} compared to the dealer's total of {total_dealer}.".format(total_player=count_total(dealt_cards_player),total_dealer=count_total(dealt_cards_dealer)))
                     else:
                            print("You have tied with scores of {total}".format(total=count_total(dealt_cards_dealer)))
              else:
                     print("The dealer has bust. You win!")
                     
# checks if player wants to play again or quit
       if count_total(dealt_cards_player) == 21 and (count_total(dealt_cards_player) > count_total(dealt_cards_dealer)):
              print("Blackjack! You Win!!!")
       while(True):
              play_again = input("Enter \"y\" to play again or enter \"q\" to quit: ")
              if (play_again == "y") or (play_again == "q"):
                     break

   