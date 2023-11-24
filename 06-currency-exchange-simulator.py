import time

print("\nCurrency Exchange Simulator.\n")
time.sleep(2)

initial_amount = None
source_currency = None

while initial_amount is None:
    try:
        initial_amount = float(input("Enter the initial amount: "))
    except ValueError:
        print("Error: Invalid Input!")

while source_currency is None:
    source_currency = input("Enter the source currency (USD/EUR/GBP/INR): ").upper()
    if source_currency not in ['USD', 'EUR', 'GBP', 'INR']:
        print("Error: Invalid Source Currency!")

target_currency = None

while target_currency is None:
    target_currency = input("Enter the target currency (USD/EUR/GBP/INR): ").upper()
    if target_currency not in ['USD', 'EUR', 'GBP', 'INR']:
        print("Error: Invalid Target Currency!")

exchange_rate = None

while exchange_rate is None:
    try:
        exchange_rate = float(input(f"Enter the exchange rate from {source_currency} to {target_currency}: "))
    except ValueError:
        print("Error: Invalid Input!")

if source_currency == 'USD':
    converted_amount = initial_amount * exchange_rate
    print(f"{initial_amount} {source_currency} is equivalent to {converted_amount:.2f} {target_currency}.")
elif source_currency == 'EUR':
    converted_amount = initial_amount / exchange_rate
    print(f"{initial_amount} {source_currency} is equivalent to {converted_amount:.2f} {target_currency}.")
elif source_currency == 'GBP':
    converted_amount = initial_amount / exchange_rate
    print(f"{initial_amount} {source_currency} is equivalent to {converted_amount:.2f} {target_currency}.")
elif source_currency == 'INR':
    converted_amount = initial_amount * exchange_rate
    print(f"{initial_amount} {source_currency} is equivalent to {converted_amount:.2f} {target_currency}.")

if converted_amount > initial_amount:
    print(f"You gained {converted_amount - initial_amount:.2f} {target_currency}.")
elif converted_amount < initial_amount:
    print(f"You incurred a loss of {initial_amount - converted_amount:.2f} {target_currency}.")
else:
    print("No gains or losses.")
