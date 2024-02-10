import random

class ATM:
    def __init__(self):
        self.accounts = {}  # Dictionary to store account balances with account numbers
        self.logged_in = False
        self.current_account = None

    def generate_account_number(self):
        return random.randint(10000, 99999)

    def create_account(self):
        account_number = self.generate_account_number()
        pin = input("Create a 4-digit PIN for your account: ")
        balance = float(input("Enter initial balance: $"))
        
        self.accounts[account_number] = {'pin': pin, 'balance': balance}
        print(f"Account created successfully. Your account number is: {account_number}")

    def login(self):
        account_number = int(input("Enter your account number: "))
        pin = input("Enter your 4-digit PIN: ")

        if account_number in self.accounts and self.accounts[account_number]['pin'] == pin:
            self.current_account = account_number
            self.logged_in = True
            print("Login successful.")
        else:
            print("Invalid account number or PIN. Please try again.")

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Logout")

    def check_balance(self):
        print(f"Current Balance: ${self.accounts[self.current_account]['balance']}")

    def withdraw_cash(self):
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= self.accounts[self.current_account]['balance']:
            self.accounts[self.current_account]['balance'] -= amount
            print(f"Withdrawal successful. Remaining Balance: ${self.accounts[self.current_account]['balance']}")
        else:
            print("Insufficient funds.")

    def deposit_cash(self):
        amount = float(input("Enter deposit amount: $"))
        self.accounts[self.current_account]['balance'] += amount
        print(f"Deposit successful. New Balance: ${self.accounts[self.current_account]['balance']}")

    def change_pin(self):
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.accounts[self.current_account]['pin'] = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid PIN. Please enter a 4-digit numeric PIN.")

    def run(self):
        while True:
            if not self.logged_in:
                print("\nWelcome to the ATM")
                print("1. Create Account")
                print("2. Login")
                print("3. Exit")

                choice = input("Enter your choice (1-3): ")

                if choice == '1':
                    self.create_account()
                elif choice == '2':
                    self.login()
                elif choice == '3':
                    print("Exiting. Thank you!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            else:
                self.display_menu()
                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    self.check_balance()
                elif choice == '2':
                    self.withdraw_cash()
                elif choice == '3':
                    self.deposit_cash()
                elif choice == '4':
                    self.change_pin()
                elif choice == '5':
                    print("Logging out. Thank you!")
                    self.logged_in = False
                    self.current_account = None
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
