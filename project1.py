class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Current Balance: ₹", self.balance)


# Creating object
account = BankAccount("Azeem", "1234567890", 5000)

account.display_balance()

account.deposit(2000)
account.display_balance()

account.withdraw(1500)
account.display_balance()

account.withdraw(10000)