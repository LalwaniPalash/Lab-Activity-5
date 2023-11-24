import time

print("\nInteger Classifier.\n")
time.sleep(2)

number = None

while number is None:
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Error: Invalid Input!")

if number > 0:
    print(f"{number} is a positive integer.")
elif number < 0:
    print(f"{number} is a negative integer.")
else:
    print(f"{number} is zero.")

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
