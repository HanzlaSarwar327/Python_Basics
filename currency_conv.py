import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if "error" in data:
        print("Invalid currency code.")
        return None
    
    rates = data["rates"]
    return rates.get(to_currency)

def currency_converter():
    print("Welcome to the Currency Converter!")
    from_currency = input("Enter the base currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()
    
    rate = get_exchange_rate(from_currency, to_currency)
    
    if rate:
        amount = float(input(f"Enter the amount in {from_currency}: "))
        converted_amount = amount * rate
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    currency_converter()
