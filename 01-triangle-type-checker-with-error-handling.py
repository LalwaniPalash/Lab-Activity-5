import time

print("\nTriangle Type Checker.\n")
time.sleep(2)

side1, side2, side3 = None, None, None

while side1 is None:
    try:
        side1 = float(input("Enter the length of the first side: "))
    except ValueError:
        print("Error: Invalid Input!")

while side2 is None:
    try:
        side2 = float(input("Enter the length of the second side: "))
    except ValueError:
        print("Error: Invalid Input!")

while side3 is None:
    try:
        side3 = float(input("Enter the length of the third side: "))
    except ValueError:
        print("Error: Invalid Input!")

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("The triangle is an equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is an isosceles triangle.")
    else:
        print("The triangle is a scalene triangle.")
    
    if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
        print("The triangle is also a right-angled triangle.")
else:
    print("Error: The given sides do not form a valid triangle.")
