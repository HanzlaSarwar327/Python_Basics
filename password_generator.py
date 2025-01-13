# Password Generator

import random
import string

def generate_password(length):
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    password_generator()
