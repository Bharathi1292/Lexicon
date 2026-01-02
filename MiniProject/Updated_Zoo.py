import random

# BASE ANIMAL

class Animal:
    MAX_ENERGY = 100
    ENERGY_PROFILE = {}

    def __init__(self, name, age, energy=50):
        self.name = name
        self.age = age
        self.energy = energy
        self.alive = True

    def change_energy(self, action):
        change = self.ENERGY_PROFILE.get(action, 0)
        self.energy = max(0, min(self.energy + change, self.MAX_ENERGY))
        if self.energy == 0:
            self.die()

    def die(self):
        self.alive = False
        print(f"{self.name} has died.")

    def sleep(self):
        self.change_energy("sleep")
        print(f"{self.name} sleeps. Energy: {self.energy}")

    def act(self, zoo):
        raise NotImplementedError("Each animal must implement act()")


# DIET TYPES 
class Herbivore(Animal):
    def eat(self):
        self.change_energy("eat")
        print(f"{self.name} eats plants. Energy: {self.energy}")


class Carnivore(Animal):
    def hunt(self, zoo):
        prey_list = [a for a in zoo.animals if isinstance(a, Herbivore) and a.alive]

        if prey_list:
            victim = random.choice(prey_list)
            victim.die()
            self.change_energy("hunt_success")
            print(f"{self.name} hunts {victim.name}! Energy: {self.energy}")
        else:
            self.change_energy("hunt_fail")
            print(f"{self.name} finds no prey. Energy: {self.energy}")


#CONCRETE ANIMALS
class Lion(Carnivore):
    ENERGY_PROFILE = {
        "hunt_success": 30,
        "hunt_fail": -10,
        "sleep": 10,
        "idle": -5
    }

    def act(self, zoo):
        if self.energy < 70 or random.random() < 0.3:
            self.hunt(zoo)
        else:
            print(f"{self.name} rests in the shade.")
            self.change_energy("idle")


class Elephant(Herbivore):
    ENERGY_PROFILE = {
        "eat": 15,
        "sleep": 10,
        "idle": -5
    }

    def splash(self):
        print(f"{self.name} splashes water happily.")
        self.change_energy("idle")

    def act(self, zoo):
        if self.energy < 60:
            self.eat()
        else:
            self.splash()


class Monkey(Herbivore):
    ENERGY_PROFILE = {
        "eat": 15,
        "play": -10,
        "sleep": 10
    }

    def play(self):
        print(f"{self.name} plays with other monkeys.")
        self.change_energy("play")

    def climb(self):
        print(f"{self.name} climbs trees energetically.")
        self.change_energy(-5)

    def act(self, zoo):
        if self.energy > 30:
            self.play()
            self.climb()
        else:
            self.eat()

class Giraffe(Herbivore):
    ENERGY_PROFILE = {
        "eat": 20,
        "sleep": 10,
        "idle": -5
    }

    def act(self, zoo):
        if self.energy < 60:
            self.eat()
        else:
            print(f"{self.name} watches the horizon.")
            self.change_energy("idle")

# VISITOR 

class Visitor:
    def __init__(self, name):
        self.name = name

    def feed(self, animal):
        if animal.alive and isinstance(animal, Herbivore):
            print(f"{self.name} feeds {animal.name}.")
            animal.eat()


# ZOO 
class Zoo:
    def __init__(self):
        self.animals = []
        self.visitors = []
        self.day = 1

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def simulate_day(self):
        print(f"\n===== DAY {self.day} =====")
        for visitor in self.visitors:
            for animal in self.animals:
                if animal.alive and random.random() < 0.3:
                    visitor.feed(animal)

        for animal in self.animals:
            if animal.alive:
                animal.act(self)

        for animal in self.animals:
            if animal.alive:
                animal.sleep()

        self.animals = [a for a in self.animals if a.alive]

        self.day += 1

    def run(self, days):
        for _ in range(days):
            if not self.animals:
                print("All animals are gone. Simulation ends.")
                break
            self.simulate_day()


#EXECUTION 
if __name__ == "__main__":
    zoo = Zoo()

  
    zoo.add_visitor(Visitor("Bharathi"))
    zoo.add_visitor(Visitor("Dibbidi"))
    zoo.add_animal(Lion("Simba", 5, energy=30))  
    zoo.add_animal(Elephant("Ele", 12))
    zoo.add_animal(Monkey("Mon", 4))
    zoo.add_animal(Monkey("Kothi", 3))
    zoo.run(days=3)
