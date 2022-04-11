#Number Guessing Game Objectives:
import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)

def check_number(user_choice,random_number,turns):
    if user_choice>random_number:
        print("Too high.")
        return turns -1
    elif user_choice < random_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You've got this, The number was {random_number}")

def set_difficulty():
    level=input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
def game():        
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    
    random_number=random.randint(1,100)
    
    attempts = set_difficulty()
    user_choice = 0
    while user_choice != random_number:
        print(f"You have {attempts} of attempts remaining to guess the number.")
        user_choice = int(input("Make a guess: ")) 
        attempts=check_number(user_choice, random_number, attempts) #overwriting the local variable

        if attempts == 0:
            print(f"You've run out of guesses, you lose, the number was {random_number}")
            return # for exit the function
        elif user_choice != random_number:
            print("Guess again.")
game()











