# Define a class
class Car:
    def __init__(self, speed):
        self.speed = speed 

    def drive_time(self, distance):
        
        time = distance / self.speed
        print(f"Time to travel {distance} km at {self.speed} km/h: {time:.2f} hours")

    def update_speed(self, new_speed):
        
        self.speed = new_speed
        print(f"Speed updated to {self.speed} km/h")


car = Car(60)
car.drive_time(120)  


car.update_speed(80)

car.drive_time(120)
