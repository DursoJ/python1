"""
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.

==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
"""

def main():
    rates = {
        "USD_EUR": 0.85,        #all rates retrieved from oanda.com currency converter
        "EUR_USD": 1.17,        #convert left currency to right
        "USD_GBP": 0.74,
        "GBP_USD": 1.36,
        "EUR_GBP": 0.87,
        "GBP_EUR": 1.16
    }
    #show all available choices
    print("Available currency pairs:")
    for pair in rates.keys():
        print(f" - {pair}")

    #get input
    pair = input("Please choose a currency pair (e.g., USD_EUR): ").upper()

    #error handling for choosing incorrect pair
    if pair not in rates:
        print("Error: Invalid currency pair.")
        return

    #error handling for negative and non-numeric
    try:
        amount = float(input(f"Enter the amount in {pair.split('_')[0]}: "))
        if amount < 0:
            print("Error: Amount cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    #conversion
    rate = rates[pair]
    converted = amount * rate
    #output
    print(f"{amount:.2f} {pair.split('_')[0]} = {converted:.2f} {pair.split('_')[1]}")

if __name__ == "__main__":
    main()