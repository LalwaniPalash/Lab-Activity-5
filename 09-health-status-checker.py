import time

print("\nHealth Status Checker\n")
time.sleep(2)

try:
    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = float(input("Enter your height in meters: "))
except ValueError:
    print("Invalid input. Please enter valid numerical values for weight and height.")
    exit()

try:
    blood_pressure = input("Enter your blood pressure reading (e.g., 120/80): ")
except ValueError:
    print("Invalid blood pressure format. Please use the format 'systolic/diastolic'.")
    exit()

try:
    systolic, diastolic = map(int, blood_pressure.split('/'))
except ValueError:
    print("Invalid blood pressure format. Please use the format 'systolic/diastolic'.")
    exit()
 
bmi = weight_kg / (height_m ** 2)

if bmi < 16.0:
    category = "Severely Underweight"
elif 16.0 <= bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25.0:
    category = "Normal"
elif 25.0 <= bmi < 30.0:
    category = "Overweight"
elif 30.0 <= bmi < 35.0:
    category = "Moderately Obese"
elif 35.0 <= bmi < 40.0:
    category = "Severely Obese"
else:
    category = "Morbidly Obese"

print(f"The BMI of a person with weight {weight_kg} kg and height {height_m} meters is {bmi:.1f} and belongs to the {category} category.")
print("The data used for calculation was provided by WHO.")

if category in ["Severely Underweight", "Underweight"]:
        print("Consider consulting with a healthcare professional to address your underweight condition.")
elif category in ["Overweight", "Moderately Obese", "Severely Obese", "Morbidly Obese"]:
        print("Consider adopting a healthier lifestyle and consulting with a healthcare professional to address your weight condition.")


if 90 <= systolic <= 120 and 60 <= diastolic <= 80:
    print("Your blood pressure is normal.")
else:
    if systolic > 120:
        print("Your systolic blood pressure is elevated. Consider monitoring your blood pressure and consulting with a healthcare professional.")
    if diastolic > 80:
        print("Your diastolic blood pressure is elevated. Consider monitoring your blood pressure and consulting with a healthcare professional.")
    
    # Check for low blood pressure
    if systolic < 90:
        print("Your systolic blood pressure is low. Ensure you stay hydrated and consider consulting with a healthcare professional.")
    if diastolic < 60:
        print("Your diastolic blood pressure is low. Ensure you stay hydrated and consider consulting with a healthcare professional.")
