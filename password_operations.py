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

    password_list = []

    password_list.append(random.choice(string.ascii_lowercase))
    password_list.append(random.choice(string.ascii_uppercase))


    all_characters = string.ascii_letters

    if include_numbers == "yes":
        password_list.append(random.choice(string.digits))
        all_characters += string.digits

    if include_special == "yes":
        password_list.append(random.choice(string.punctuation))
        all_characters += string.punctuation

    remaining_length = length-len(password_list)


    for _ in range(length):
        password_list.append(random.choice(all_characters))
    
    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Generated Strong Password: {password}")