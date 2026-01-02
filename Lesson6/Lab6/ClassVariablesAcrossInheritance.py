class Vehicle:
    wheels = 4  

class Bike(Vehicle):
    wheels = 2  

class Car(Vehicle):
    pass  

v = Vehicle()
b = Bike()
c = Car()

print("Vehicle wheels =", v.wheels)
print("Bike wheels =", b.wheels)
print("Car wheels =", c.wheels)
