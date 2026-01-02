class BankAccount:
    def show_balance(self):
        print("Account Balance is : 1000")

class SavingsAccount(BankAccount):
    def show_balance(self):
        super().show_balance() 
        print("Interest will be added soon")


account = SavingsAccount()
account.show_balance()
