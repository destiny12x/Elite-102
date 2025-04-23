# Banking System


accounts = {
    '123456': {'pin': '1234', 'name': 'Alice', 'balance': 1000.0},
    '654321': {'pin': '4321', 'name': 'Bob', 'balance': 500.0}
}

current_user = None

def login():
    global current_user
    print("\n=== Banking System Login ===")
    acc_num = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if acc_num in accounts and accounts[acc_num]['pin'] == pin:
        current_user = acc_num
        print(f"\nLogin successful. Welcome, {accounts[acc_num]['name']}!")
        main_menu()
    else:
        print("Invalid account number or PIN.\n")

def check_balance():
    balance = accounts[current_user]['balance']
    print(f"\nYour current balance is: ${balance}\n")

def deposit():
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            accounts[current_user]['balance'] += amount
            print(f"${amount} deposited successfully.\n")
        else:
            print("Amount must be positive.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def withdraw():
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if 0 < amount <= accounts[current_user]['balance']:
            accounts[current_user]['balance'] -= amount
            print(f"${amount} withdrawn successfully.\n")
        else:
            print("Insufficient balance or invalid amount.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def edit_account():
    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. PIN")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        new_name = input("Enter your new name: ")
        accounts[current_user]['name'] = new_name
        print("Name updated successfully.\n")
    elif choice == '2':
        new_pin = input("Enter your new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            accounts[current_user]['pin'] = new_pin
            print("PIN updated successfully.\n")
        else:
            print("PIN must be 4 digits.\n")
    else:
        print("Invalid option.\n")

def close_account():
    global current_user
    confirm = input("Are you sure you want to close your account? (yes/no): ").lower()
    if confirm == 'yes':
        del accounts[current_user]
        print("Account closed successfully.\n")
        current_user = None
    else:
        print("Account closure canceled.\n")

def logout():
    global current_user
    print(f"\nLogging out {accounts[current_user]['name']}...\n")
    current_user = None

def create_account():
    print("\n=== Create New Account ===")
    acc_num = input("Enter a new account number: ")
    if acc_num in accounts:
        print("Account number already exists.\n")
        return

    name = input("Enter your name: ")
    pin = input("Set a 4-digit PIN: ")
    try:
        balance = float(input("Initial deposit amount: $"))
    except ValueError:
        print("Invalid deposit amount.\n")
        return

    if len(pin) == 4 and pin.isdigit() and balance >= 0:
        accounts[acc_num] = {'name': name, 'pin': pin, 'balance': balance}
        print("Account created successfully!\n")
    else:
        print("Invalid PIN or balance.\n")

def main_menu():
    while current_user:
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Edit Account")
        print("5. Close Account")
        print("6. Logout")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            edit_account()
        elif choice == '5':
            close_account()
        elif choice == '6':
            logout()
        else:
            print("Invalid option. Try again.\n")

def home():
    while True:
        print("=== Welcome to the Banking System ===")
        print("1. Login")
        print("2. Create New Account")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            login()
        elif choice == '2':
            create_account()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

# Start the Banking System
home()