class Car:
    wheels = 4  
    def __init__(self, brand, color):
        self.brand = brand  
        self.color = color  
    
    def car_info_class(self):
        print(f"{self.brand} has {Car.wheels} wheels")

    
    def car_info_instance(self):
        print(f"{self.brand} is {self.color}")


car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")


print("Initial car info:")
car1.car_info_class()
car2.car_info_class()
car1.car_info_instance()
car2.car_info_instance()


Car.wheels = 6
print("\nAfter changing class attribute (wheels):")
car1.car_info_class()
car2.car_info_class()


car1.color = "Green"
print("\nAfter changing car1's color (instance attribute):")
car1.car_info_instance()
car2.car_info_instance()
