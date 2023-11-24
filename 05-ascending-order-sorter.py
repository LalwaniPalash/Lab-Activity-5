import time

print("\nThree inputs to Ascending Order.\n")
time.sleep(2)

num1, num2, num3 = None, None, None

while num1 is None:
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Error: Invalid Input!")

while num2 is None:
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid Input!")

while num3 is None:
    try:
        num3 = float(input("Enter the third number: "))
    except ValueError:
        print("Error: Invalid Input!")

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(f"The numbers in ascending order are: {num1}, {num2}, {num3}")
    else:
        print(f"The numbers in ascending order are: {num1}, {num3}, {num2}")
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(f"The numbers in ascending order are: {num2}, {num1}, {num3}")
    else:
        print(f"The numbers in ascending order are: {num2}, {num3}, {num1}")
else:
    if num1 <= num2:
        print(f"The numbers in ascending order are: {num3}, {num1}, {num2}")
    else:
        print(f"The numbers in ascending order are: {num3}, {num2}, {num1}")
