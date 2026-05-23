from password_operations import generate_password 

def show_menu():
    print("\n" + "*" *40)
    print("   PASSWORD GENERATOR SYSTEM   ")
    print("*" * 40)
    print("1. Generate Password")
    print("2. Exit")

def main():
    while True:
        show_menu()

        choice = input("Enter your choice(1-2): ")

        if choice == "1":
            generate_password()

        elif choice == "2":
            generate_password()

        else:
            print("\nInvalid choice! Please enter 1 or 2.")

main()