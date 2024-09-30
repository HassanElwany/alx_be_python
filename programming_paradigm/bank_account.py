class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        # display the current balance
        print(f"Current Balance: ${self.account_balance}")

    def __str__(self):
        return f"Your balance is {self.account_balance}"
