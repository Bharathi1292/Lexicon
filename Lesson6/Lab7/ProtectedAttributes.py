class BankAccount:
    def __init__(self, balance):
        self._balance = balance  

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount  
        print(f"Deposited amount is {amount}, new balance is {self._balance}")

    def display_balance(self):
        print("Current balance is :", self._balance) 

account = SavingsAccount(1000)
account.display_balance()
account.deposit(500)
account.display_balance()
