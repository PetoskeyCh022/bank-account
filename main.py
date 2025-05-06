# Charles
# 5/6/2025
# Three Ways to Modify BankAccount Class Attributes
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.account_holder} has deposited {amount}.\n{self.account_holder}'s new balance is: {self.balance}")
        else:
            print("Invalid deposit amount. You can't deposit nothing.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} has withdrawn {amount}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance
    
    def display_account_info(self):
        print(f"Account holder: {self.account_holder}\nBalance: {self.balance}")


me = BankAccount("Charles", 1500)
me.display_account_info()

me.balance = 2000
me.display_account_info()

me.deposit(700)
me.display_account_info()

me.withdraw(200)
me.display_account_info()

me.withdraw(1000000)
me.display_account_info()

        