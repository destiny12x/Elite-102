import tkinter as tk

# --- Banking System Logic ---
class BankingSystem:
    def __init__(self):
        self.accounts = {
            '123456': {'pin': '1234', 'name': 'Alice', 'balance': 1000.0},
            '654321': {'pin': '4321', 'name': 'Bob', 'balance': 500.0}
        }
        self.current_user = None

    def login(self, acc_num, pin):
        if acc_num in self.accounts and self.accounts[acc_num]['pin'] == pin:
            self.current_user = acc_num
            return f"Welcome, {self.accounts[acc_num]['name']}!"
        else:
            return "Invalid account number or PIN."

    def check_balance(self):
        if self.current_user:
            return f"Your balance is: ${self.accounts[self.current_user]['balance']:.2f}"
        return "Please log in first."

    def deposit(self, amount):
        if self.current_user and amount > 0:
            self.accounts[self.current_user]['balance'] += amount
            return f"${amount} deposited."
        return "Invalid amount or not logged in."

    def withdraw(self, amount):
        if self.current_user:
            if 0 < amount <= self.accounts[self.current_user]['balance']:
                self.accounts[self.current_user]['balance'] -= amount
                return f"${amount} withdrawn."
            else:
                return "Insufficient balance or invalid amount."
        return "Please log in first."


# --- GUI Setup ---
bank = BankingSystem()
root = tk.Tk()
root.title("Elite 102 Banking System")

# --- Login Section ---
tk.Label(root, text="Account Number:").grid(row=0, column=0)
account_entry = tk.Entry(root)
account_entry.grid(row=0, column=1)

tk.Label(root, text="PIN:").grid(row=1, column=0)
pin_entry = tk.Entry(root, show="*")
pin_entry.grid(row=1, column=1)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=2, column=0, columnspan=2)

def try_login():
    acc = account_entry.get()
    pin = pin_entry.get()
    message = bank.login(acc, pin)
    result_label.config(text=message)
    if "Welcome" in message:
        show_main_menu()

tk.Button(root, text="Login", command=try_login).grid(row=3, column=0, columnspan=2)

# --- Banking Actions ---
def show_main_menu():
    # Hide login widgets
    account_entry.grid_remove()
    pin_entry.grid_remove()
    for widget in root.grid_slaves(row=0):
        widget.grid_remove()
    for widget in root.grid_slaves(row=1):
        widget.grid_remove()
    for widget in root.grid_slaves(row=3):
        widget.grid_remove()

    # Entry for amount
    tk.Label(root, text="Amount:").grid(row=4, column=0)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=4, column=1)

    # Functions for actions
    def do_deposit():
        try:
            amt = float(amount_entry.get())
            result = bank.deposit(amt)
            result_label.config(text=result)
        except ValueError:
            result_label.config(text="Enter a valid number.")

    def do_withdraw():
        try:
            amt = float(amount_entry.get())
            result = bank.withdraw(amt)
            result_label.config(text=result)
        except ValueError:
            result_label.config(text="Enter a valid number.")

    def do_balance():
        result = bank.check_balance()
        result_label.config(text=result)

    # Buttons for actions
    tk.Button(root, text="Check Balance", command=do_balance).grid(row=5, column=0, columnspan=2)
    tk.Button(root, text="Deposit", command=do_deposit).grid(row=6, column=0)
    tk.Button(root, text="Withdraw", command=do_withdraw).grid(row=6, column=1)
    tk.Button(root, text="Exit", command=root.quit).grid(row=7, column=0, columnspan=2)

# --- Run the App ---
root.mainloop()