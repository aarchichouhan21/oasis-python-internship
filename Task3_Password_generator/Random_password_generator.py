import random
import string

# Ask user for password length
length = int(input("Enter the password length: "))

# Ask user what characters to include
use_lower = input("Include lowercase letters? (y/n): ")
use_upper = input("Include uppercase letters? (y/n): ")
use_digits = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = ""

if use_lower == 'y':
    characters += string.ascii_lowercase

if use_upper == 'y':
    characters += string.ascii_uppercase

if use_digits == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation

# Check if at least one option was selected
if characters == "":
    print("Error: You must select at least one character type.")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
