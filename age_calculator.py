from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def age_calculator():
    print("Welcome to the Age Calculator!")
    dob_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(dob_str, "%Y-%m-%d")
    age = calculate_age(birthdate)
    print(f"You are {age} years old.")

if __name__ == "__main__":
    age_calculator()
