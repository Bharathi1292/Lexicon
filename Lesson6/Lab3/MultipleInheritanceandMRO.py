class BaseValue:
    def __init__(self):
        self.value = 10
        print("Constructor of BaseValue : value =", self.value)

class AddBonus:
    def __init__(self):
        super().__init__()
        self.value += 20
        print("Constructor of AddBonus : value =", self.value)

class CalculateTotal(AddBonus, BaseValue):
    def __init__(self):
        super().__init__()
        self.value += 30
        print("Constructor of CalculateTotal : value =", self.value)

obj = CalculateTotal()

print("Final value =", obj.value)
print("MRO of CalculateTotal =", CalculateTotal.mro())
