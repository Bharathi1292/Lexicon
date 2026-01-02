class Vehicle:
    vehicle_count = 0  

    def __init__(self, name, max_speed):
        self.name = name
        self._max_speed = max_speed  
        Vehicle.vehicle_count += 1

    def vehicle_info(self):
        return f"Vehicle Name: {self.name}, Max Speed: {self._max_speed} km/h"

class Car(Vehicle):
    def __init__(self, name, max_speed, num_doors):
        super().__init__(name, max_speed)
        self.num_doors = num_doors

    def vehicle_info(self):
        base_info = super().vehicle_info()
        return f"{base_info}, Doors: {self.num_doors}"

class Bike(Vehicle):
    def __init__(self, name, max_speed, has_carrier):
        super().__init__(name, max_speed)
        self.has_carrier = has_carrier

    def vehicle_info(self):
        base_info = super().vehicle_info()
        carrier_status = "Yes" if self.has_carrier else "No"
        return f"{base_info}, Carrier: {carrier_status}"

v1 = Vehicle("Generic Vehicle", 100)
c1 = Car("Sedan", 180, 4)
b1 = Bike("Mountain Bike", 50, True)

print(v1.vehicle_info())
print(c1.vehicle_info())
print(b1.vehicle_info())

print("Total Vehicles Created:", Vehicle.vehicle_count)
