import random
import os
from art import logo

# Function to clear the console
clear = lambda: os.system('cls')

# List of cards in the deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to start a new game
def start_a_game():
   while True:
      # Asks the player if they want to play a new game
      play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
      if play == 'y':
         blackjack()  # Starts a new game of Blackjack
      else:
         break

# Main function of the Blackjack game
def blackjack():
   clear()  # Clears the console

   print(logo)  # Prints the game logo

   # Deals cards for the player and the computer
   user_cards = random.sample(cards, 2)
   computer_cards = random.sample(cards, 2)

   # Calculates the total score of the player and the computer
   user_total_cards = sum(user_cards)
   computer_total_cards = sum(computer_cards)

   # Prints the player's cards and the computer's first card
   print(f"Your cards: {user_cards}, current score: {user_total_cards}")
   print(f"Computer's first card: {computer_cards[0]}")

   # Loop to allow the player to get more cards (if desired)
   while True:
      new_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if new_card == 'y':
         # The player gets a new card
         new_card_value = random.choice(cards)
         user_cards.append(new_card_value)
         user_total_cards += new_card_value   

         # Checks if the player has an Ace (11) and went over 21, changing it to 1
         if user_total_cards > 21 and 11 in user_cards:
            user_total_cards -= 10  # Subtracts 10 to change the Ace from 11 to 1
            user_cards[user_cards.index(11)] = 1

         # Prints the player's cards and the computer's first card again
         print(f"Your cards: {user_cards}, current score: {user_total_cards}")
         print(f"Computer's first card: {computer_cards[0]}")

         # If the player goes over 21, they lose
         if user_total_cards > 21:
            print("You went over. You lose.")
            return
      else:
         break

   # The computer gets cards until its score is at least 17
   while computer_total_cards < 17:
      computer_cards.append(random.choice(cards))
      computer_total_cards += computer_cards[-1]

   # Prints the final hands of the player and the computer
   print(f"Your final hand: {user_cards}, final score: {user_total_cards}")
   print(f"Computer's final hand: {computer_cards}, final score: {computer_total_cards}")

   # Checks who won the game
   if user_total_cards == 21:
      print("You have a blackjack. You won!")
   elif computer_total_cards == 21:
      print("Opponent has a blackjack. You lost!")
   elif computer_total_cards > 21:
      print("Opponent went over. You won!")
   elif user_total_cards > computer_total_cards:
      print("You won!")
   elif user_total_cards < computer_total_cards:
      print("You lost!")
   else:
      print("It's a draw!")

# Starts the game
start_a_game()
