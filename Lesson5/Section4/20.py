class BankAccount:
    def __init__(self, **kwargs):
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        if not hasattr(self, "_balance"):
            self._balance = 0.0
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
    def __str__(self):
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        attr_str = ", ".join(f"{k}: {v}" for k, v in attrs.items())
        return f"BankAccount({attr_str}, balance: {self._balance})"
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance == other.balance
    def apply_interest(self, rate):
      
        self._balance += self._balance * rate
        return self._balance
account1 = BankAccount(owner="Bharathi", account_number=12345, _balance=1000)
account2 = BankAccount(owner="Dibbidi", account_number=67890, _balance=1000)
print(account1.balance)  
account1.apply_interest(0.05)
print(account1.balance) 
print(account1)
print(account1 == account2)  
