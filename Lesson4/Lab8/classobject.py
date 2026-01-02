class Car:
    wheels = 4  
    def __init__(self, brand, color):
        self.brand = brand  
        self.color = color  

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")


print(f"{car1.brand} has {car1.wheels} wheels")
print(f"{car2.brand} has {car2.wheels} wheels")

car1.wheels = 6

print("\nAfter modifying car1's wheels:")
print(f"{car1.brand} has {car1.wheels} wheels")  
print(f"{car2.brand} has {car2.wheels} wheels")  
