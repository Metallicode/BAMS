accounts = {}  # Dictionary to store account data

def create_account():
    # Generate account and get user details
    pass

def login():
    # Authenticate user and allow account actions
    pass

def main():
    while True:
        # Display main menu and prompt user for action
        action = input("Choose an action: (1) Create Account, (2) Login, (3) Exit: ")
        if action == "1":
            create_account()
        elif action == "2":
            login()
        elif action == "3":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
