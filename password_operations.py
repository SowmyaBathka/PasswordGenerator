import random
import string


def generate_password():
    print("\n--- Generate Password ---")

    length = input("Enter password length: ")

    if not length.isdigit():
        print("Please enter a valid number.")
        return

    length = int(length)

    include_numbers=input("Include numbers? (yes/no):").strip().lower()
    include_special=input("Include special characters? (yes/no):").strip().lower()

    password_characters = string.ascii_letters

    if include_numbers == "yes":
        password_characters += string.digits

    if include_special == "yes":
        password_characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(password_characters)

    print(f"Generated Password: {password}")