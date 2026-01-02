import random

class Animal:
    MAX_ENERGY = 100
    ENERGY_PROFILE = {}

    def __init__(self, name, age, energy=50):
        self.name = name
        self.age = age
        self.energy = energy
        self.alive = True

    def change_in_energy(self, action):
        change = self.ENERGY_PROFILE.get(action, 0)
        self.energy = max(0, min(self.energy + change, self.MAX_ENERGY))

        if self.energy == 0:
            self.alive = False
            print(f"{self.name} has no energy left and dies.")

    def sleep(self):
        self.change_in_energy("sleep")
        print(f"{self.name} sleeps. Energy: {self.energy}")

    def act(self, zoo):
        pass

    def __str__(self):
        return f"{self.name} (Energy: {self.energy})"

# DIET TYPES 

class Herbivore(Animal):
    def eat(self):
        self.change_in_energy("eat")
        print(f"{self.name} eats plants. Energy: {self.energy}")


class Carnivore(Animal):
    def hunt(self, zoo):
        prey = [a for a in zoo.animals if isinstance(a, Herbivore) and a.alive]

        if prey:
            victim = random.choice(prey)
            victim.alive = False
            self.change_in_energy("hunt_success")
            print(f"{self.name} hunts {victim.name}! Energy: {self.energy}")
        else:
            self.change_in_energy("hunt_fail")
            print(f"{self.name} finds no prey. Energy: {self.energy}")


# CONCRETE ANIMALS 

class Lion(Carnivore):
    ENERGY_PROFILE = {
        "hunt_success": 30,
        "hunt_fail": -10,
        "sleep": 10,
        "idle": -5
    }

    def act(self, zoo):
        if self.energy < 40:
            self.hunt(zoo)
        else:
            print(f"{self.name} rests in the shade.")
            self.change_in_energy("idle")


class Elephant(Herbivore):
    ENERGY_PROFILE = {
        "eat": 15,
        "sleep": 10,
        "idle": -5
    }

    def act(self, zoo):
        if self.energy < 60:
            self.eat()
        else:
            print(f"{self.name} splashes water.")
            self.change_in_energy("idle")


class Monkey(Herbivore):
    ENERGY_PROFILE = {
        "eat": 15,
        "play": -10,
        "sleep": 10
    }

    def act(self, zoo):
        if self.energy > 30:
            print(f"{self.name} plays with other monkeys.")
            self.change_in_energy("play")
        else:
            self.eat()


#VISITOR 
class Visitor:
    def __init__(self, name):
        self.name = name

    def feed(self, animal):
        if animal.alive and isinstance(animal, Herbivore):
            print(f"{self.name} feeds {animal.name}.")
            animal.eat()


#  ZOO 

class Zoo:
    def __init__(self):
        self.animals = []
        self.day = 1

    def add_animal(self, animal):
        self.animals.append(animal)

    def simulate_day(self):
        print(f"\n===== DAY {self.day} =====")

        visitor = Visitor("Alice")
        for animal in self.animals:
            if animal.alive and random.random() < 0.3:
                visitor.feed(animal)

        # Animal actions
        for animal in self.animals:
            if animal.alive:
                animal.act(self)

        # Animals sleep
        for animal in self.animals:
            if animal.alive:
                animal.sleep()

        # Remove dead animals
        self.animals = [a for a in self.animals if a.alive]

        self.day += 1

    def run(self, days):
        for _ in range(days):
            if not self.animals:
                print("All animals are gone. Simulation ends.")
                break
            self.simulate_day()


if __name__ == "__main__":
    zoo = Zoo()

    zoo.add_animal(Lion("Simba", 5))
    zoo.add_animal(Elephant("Ele", 12))
    zoo.add_animal(Monkey("Mon", 4))
    zoo.add_animal(Monkey("kothi", 3))

    zoo.run(days=3)
