# Dice Roller Simulator

import random

def roll_dice():
    print("Welcome to the Dice Roller Simulator!")
    print("Type 'roll' to roll the dice or 'exit' to quit the simulator.")
    
    while True:
        user_input = input("\nEnter your command: ").lower()
        if user_input == "roll":
            dice_value = random.randint(1, 6)
            print(f"The dice rolled: {dice_value}")
        elif user_input == "exit":
            print("Thanks for using the Dice Roller Simulator! Goodbye!")
            break
        else:
            print("Invalid command. Type 'roll' or 'exit'.")

if __name__ == "__main__":
    roll_dice()
