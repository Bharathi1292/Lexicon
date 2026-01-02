class Vehicle:
    def __init__(self):
        super().__init__()
        print("constructor of Vehicle")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("constructor of Car")

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        print("constructor of ElectricCar")

obj = ElectricCar()
