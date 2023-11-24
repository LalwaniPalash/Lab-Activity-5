print("\nTemperature Converter (Celsius to Fahrenheit and vice versa)\n")

temperature = None

while temperature is None:
	try:
		temperature = float(input("Enter the temperature: "))
	except ValueError:
		print("Error: Invalid Input!")

unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature} degrees Celsius is equal to {converted_temperature:.2f} degrees Fahrenheit.")
elif unit == "F":
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature} degrees Fahrenheit is equal to {converted_temperature:.2f} degrees Celsius.")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
