import time

print("\nMovie Ticket Cost Calculator\n")
time.sleep(2)

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid age.")
    exit()
try:
    showtime = input("Enter the showtime (matinee/evening): ").lower()
except ValueError:
    print("Invalid input. Please enter a valid showtime.")
    exit()

matinee_price = 100.00
evening_price = 150.00

if age < 5 or age >= 65:
    matinee_price *= 0.5
    evening_price *= 0.5

if showtime == "matinee":
    print(f"\nThe cost of the ticket for the matinee show is Rs. {matinee_price:.2f}.")
elif showtime == "evening":
    print(f"\nThe cost of the ticket for the evening show is Rs. {evening_price:.2f}.")
else:
    print("An Unknown Error Occurred. Please Try again after some time.") 
