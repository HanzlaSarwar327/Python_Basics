# Simple Unit Converter in Python

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Select a conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    
    try:
        choice = int(input("Enter the number of the conversion (1/2/3/4): "))
        if choice in [1, 2, 3, 4]:
            value = float(input("Enter the value to convert: "))
            
            if choice == 1:
                print(f"{value} kilometers is equal to {km_to_miles(value):.2f} miles.")
            elif choice == 2:
                print(f"{value} miles is equal to {miles_to_km(value):.2f} kilometers.")
            elif choice == 3:
                print(f"{value}°C is equal to {celsius_to_fahrenheit(value):.2f}°F.")
            elif choice == 4:
                print(f"{value}°F is equal to {fahrenheit_to_celsius(value):.2f}°C.")
        else:
            print("Invalid input. Please select a valid option.")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    unit_converter()
