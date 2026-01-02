class Aggregation:
    def __init__(self):
        self.value = 10
        print("Constructor of Aggregation : value =", self.value)

class Addition(Aggregation):
    def __init__(self):
        super().__init__()
        self.value += 5
        print("Constructor of Addition : value =", self.value)

class Multiplication(Addition):
    def __init__(self):
        super().__init__()
        self.value *= 2
        print("Constructor of Multiplication : value =", self.value)

obj = Multiplication()
print("Final value =", obj.value)
