class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    def apply_interest(self, rate):
        return self._balance + (self._balance * rate)

account = BankAccount(1000)

print("Balance:", account.balance)
print("After interest:", account.apply_interest(0.05))
