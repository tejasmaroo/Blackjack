import random
from art import logo
import os

def deal_cards():
    cards = [11, 2 , 3,  4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21: 
        return "You went over, You Loose! :("
    if user_score == computer_score:
        return "Draw:("
    elif computer_score == 0:
        return "Loose! Opponent has Blackjack :("
    elif user_score == 0:
        return "Win! You have a Blackjack :)"
    elif user_score > 21:
        return "You went over, You Loose! :("
    elif computer_score > 21:
        return "Opponent went over, You Win! :)"
    elif user_score > computer_score:
        return "You Win! :)"
    else:
        return "You Loose! :("
    
def game():
    
    print(logo)
    
    user_cards = []
    computer_cards = []
    game_over = False
    
    for c in range(2):
            user_cards.append(deal_cards())
            computer_cards.append(deal_cards())
    
    while game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour cards: {user_cards}, Your score: {user_score}")
        print(f"Opponent's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21: 
            game_over = True
        else:
            should_user_deal = input("\nType 'y' to get another card or type 'n' to pass: ")
            if should_user_deal == 'y':
                user_cards.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, Final score: {user_score}")
    print(f"Opponent's final hand: {computer_cards}, Final score: {computer_score}")
    print("\n"+compare(user_score, computer_score)+"\n")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    game()