# Rock, Paper, Scissors Game

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.")
    
    while True:
        user_choice = input("\nEnter your choice: ").lower()
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break
        elif user_choice in ["rock", "paper", "scissors"]:
            computer_choice = get_computer_choice()
            print(f"The computer chose: {computer_choice}")
            print(determine_winner(user_choice, computer_choice))
        else:
            print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

if __name__ == "__main__":
    rock_paper_scissors()
