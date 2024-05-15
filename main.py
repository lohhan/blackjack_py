import random
import os
from art import logo

# Função para limpar o console
clear = lambda: os.system('cls')

# Lista de cartas do baralho
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Função para iniciar um novo jogo
def start_a_game():
   while True:
      # Pergunta ao jogador se ele quer jogar um novo jogo
      play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
      if play == 'y':
         blackjack()  # Inicia um novo jogo de Blackjack
      else:
         break

# Função principal do jogo de Blackjack
def blackjack():
   clear()  # Limpa o console

   print(logo)  # Imprime o logotipo do jogo

   # Distribui cartas para o jogador e para o computador
   user_cards = random.sample(cards, 2)
   computer_cards = random.sample(cards, 2)

   # Calcula a pontuação total do jogador e do computador
   user_total_cards = sum(user_cards)
   computer_total_cards = sum(computer_cards)

   # Imprime as cartas do jogador e a primeira carta do computador
   print(f"Your cards: {user_cards}, current score: {user_total_cards}")
   print(f"Computer's first card: {computer_cards[0]}")

   # Loop para permitir que o jogador pegue mais cartas (se desejar)
   while True:
      new_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if new_card == 'y':
         # O jogador pega uma nova carta
         new_card_value = random.choice(cards)
         user_cards.append(new_card_value)
         user_total_cards += new_card_value   

         # Verifica se o jogador tem um Ás (11) e ultrapassou 21, trocando-o por 1
         if user_total_cards > 21 and 11 in user_cards:
            user_total_cards -= 10  # Subtrai 10 para mudar o Ás de 11 para 1.
            user_cards[user_cards.index(11)] = 1

         # Imprime as cartas do jogador e a primeira carta do computador novamente
         print(f"Your cards: {user_cards}, current score: {user_total_cards}")
         print(f"Computer's first card: {computer_cards[0]}")

         # Se o jogador ultrapassar 21, ele perde
         if user_total_cards > 21:
            print("You went over. You lose.")
            return
      else:
         break

   # O computador pega cartas até sua pontuação ser pelo menos 17
   while computer_total_cards < 17:
      computer_cards.append(random.choice(cards))
      computer_total_cards += computer_cards[-1]

   # Imprime as mãos finais do jogador e do computador
   print(f"Your final hand: {user_cards}, final score: {user_total_cards}")
   print(f"Computer's final hand: {computer_cards}, final score: {computer_total_cards}")

   # Verifica quem ganhou o jogo
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

# Inicia o jogo
start_a_game()
