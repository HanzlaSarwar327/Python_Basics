# Typing Speed Test

import time
import random

def typing_speed_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful programming language.",
        "Artificial intelligence is transforming the world.",
        "Practice makes perfect in coding and typing.",
        "Learning to code opens many opportunities."
    ]
    
    sentence = random.choice(sentences)
    print("Typing Speed Test!")
    print("\nType the following sentence as fast as you can:")
    print(f"\n{sentence}")
    input("\nPress Enter when you're ready...")
    
    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = len(user_input.split()) / (elapsed_time / 60)
    
    print("\nResults:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute (WPM): {words_per_minute:.2f}")
    
    if user_input == sentence:
        print("Great job! You typed the sentence correctly.")
    else:
        print("You made some mistakes. Keep practicing!")

if __name__ == "__main__":
    typing_speed_test()
