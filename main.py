from password_operations import generate_password 

def show_menu():
    print("\n" + "*" *45)
    print("   PASSWORD GENERATOR SYSTEM   ")
    print("*" * 45)
    print("1. Generate Password")
    print("2. Exit")

def main():
    while True:
        try:
            show_menu()

            choice = input("Enter your choice(1-2): ")

            if choice == "1":
                generate_password()

            elif choice == "2":
                print("\nThank you for using Password Generator!")
                break

            else:
                print("\nInvalid choice! Please enter 1 or 2.")
            
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break 

        except Exception as error:
            print("Unexpected error:",error)

main()