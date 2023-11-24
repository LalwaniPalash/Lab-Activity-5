import time

print("\nVowel and Consonant Checker.\n")
time.sleep(2)

character = None

while character is None or len(character) != 1:
    character = input("Enter a single character: ")
    if len(character) != 1:
        print("Error: Please enter only one character.")

character = character.lower()

if character.isalpha():
    if character in ('a', 'e', 'i', 'o', 'u'):
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")
else:
    print("Error: Please enter a valid alphabetic character.")
