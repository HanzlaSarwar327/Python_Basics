# Hangman Game

import random

def get_word():
    words = ["python", "programming", "hangman", "developer", "computer", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")
    word = get_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")
        
        if set(word).issubset(guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()
