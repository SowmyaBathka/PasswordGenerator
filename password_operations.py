import random
import string
from validations import validate_length,validate_count,validate_yes_no

def generate_password():
    print("\n--- Generate Password ---")

    length = input("Enter password length: ")

    if not validate_length(length):
        return

    length = int(length)

    count = input("How many passwords do you want to generate? ")

    if not validate_count(count):
        return

    count = int(count)

    include_numbers = input("Include numbers? (yes/no): ")
    if not validate_yes_no(include_numbers):
        return 
    

    include_special = input("Include special characters? (yes/no): ")
    if not validate_yes_no(include_special):
        return 

    for password_number in range(1, count + 1):
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

        remaining_length = length - len(password_list)

        for _ in range(remaining_length):
            password_list.append(random.choice(all_characters))

        random.shuffle(password_list)

        password = "".join(password_list)

        print(f"Generated Password {password_number}: {password}")