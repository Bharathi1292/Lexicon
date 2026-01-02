class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"  
class Cow:
    def speak(self):
        return "Moo!"
def animal_sound(animal):
    if isinstance(animal, Dog):
        return animal.speak()
    elif isinstance(animal, Cat):
        return animal.speak()
    elif isinstance(animal, Cow):
       return animal.speak()
d = Dog()
c = Cat()
c1 = Cow()
print(animal_sound(d)) 
print(animal_sound(c)) 
print(animal_sound(c1)) 

# Polymorphism Version
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Cow(Animal):
    def speak(self):
        return "Moo!"  
def animal_sound(animal):
    return animal.speak()
animals = [Dog(), Cat(), Cow()]
for a in animals:
    print(animal_sound(a))
