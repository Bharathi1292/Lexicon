class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Account balance: {self.balance}")
class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account  

    def deposit_money(self, amount):
        print(f"{self.name} deposits {amount}")
        self.account.deposit(amount)

    def withdraw_money(self, amount):
        print(f"{self.name} withdraws {amount}")
        self.account.withdraw(amount)

acc1 = BankAccount(500)
cust1 = Customer("Bharathi", acc1)

cust1.deposit_money(200)
acc1.show_balance()

cust1.withdraw_money(100)
acc1.show_balance()

print("\nBank updates account manually...")
acc1.balance = 1000
acc1.show_balance()

cust1.withdraw_money(300)
acc1.show_balance()
