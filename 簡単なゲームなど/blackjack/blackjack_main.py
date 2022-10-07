import random
from blackjack_art import logo
import os


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)


def check(p_score, d_score):
    if p_score > d_score:
        print("You win")
    elif d_score > p_score:
        print("You lose")
    elif p_score == d_score:
        print("draw")


def choose_a_card():
    card = random.choice(cards)
    return card


def dealer_drow():
    while sum(dealer_cards) < 17:
        card = random.choice(cards)
        dealer_cards.append(card)
        if sum(dealer_cards) > 21 and 11 in dealer_cards:
            for i, k in enumerate(dealer_cards):
                if k == 11:
                    dealer_cards[i] = 1
                    dealer_sum = sum(dealer_cards)


start = input("Type 'y' to play Blackjack: ")
if start == 'y':
    pass

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
while True:
  
    player_cards = []
    dealer_cards = []

    for i in range(2):
        player_cards.append(choose_a_card())
        dealer_cards.append(choose_a_card())

    player_sum = sum(player_cards)
    if player_sum > 21 and 11 in player_cards:
        for i in range(len(player_cards)):
            if player_cards[i] == 11:
                player_cards[i] = 1
    dealer_drow()
    dealer_sum = sum(dealer_cards)

    while True:
    
        player_sum = sum(player_cards)
        print(f" Your cards: {player_cards}, score: {player_sum}")
        print(f" computer's first card: {dealer_cards[0]}")
        ask = input("Type 'y' to get another card, type 'n' to pass: ")
        if ask == 'y':
            player_cards.append(choose_a_card())
            player_sum = sum(player_cards)
            if player_sum > 21 and 11 in player_cards:
                for i in range(len(player_cards)):
                    if player_cards[i] == 11:
                        player_cards[i] = 1
                        player_sum = sum(player_cards)

            if player_sum > 21:
                print(f" Your cards are {player_cards}, score is {player_sum}")
                print(f" Your final hand: {player_cards}, final score: {player_sum}")
                print("You lose")
        
                ask_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                if ask_continue == 'y':
                    clear()
                    print(logo)
                    player_cards = []
                    dealer_cards = []
                    for i in range(2):
                        player_cards.append(choose_a_card())
                        dealer_cards.append(choose_a_card())
                    dealer_drow()
                    dealer_sum = sum(dealer_cards)
                else:
                    break

        else:
            if dealer_sum > 21:
                print(f" Your final hand: {player_cards}, final score: {player_sum}")
                print(f" Computer's final hand: {dealer_cards}, final score: {dealer_sum}")
                print("You win")
                ask_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                if ask_continue == 'y':
                    clear()
                    print(logo)
                    player_cards = []
                    dealer_cards = []
                    for i in range(2):
                        player_cards.append(choose_a_card())
                        dealer_cards.append(choose_a_card())
                    dealer_drow()
                    dealer_sum = sum(dealer_cards)
            else:
                print(f" Your final hand: {player_cards}, final score: {player_sum}")
                print(f" Computer's final hand: {dealer_cards}, final score: {dealer_sum}")

                check(player_sum, dealer_sum)
                break

    ask_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask_continue == 'y':
        clear()
        print(logo)
        player_cards = []
        dealer_cards = []
        for i in range(2):
            player_cards.append(choose_a_card())
            dealer_cards.append(choose_a_card())
        dealer_drow()
        dealer_sum = sum(dealer_cards)
    else:
        break
