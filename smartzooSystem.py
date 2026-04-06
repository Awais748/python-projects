# 🧠 Smart Zoo System
# Concepts used:
# ✔ Multiple Inheritance
# ✔ super()
# ✔ Polymorphism


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} (Animal) initialized")

    def speak(self):
        print("Animal makes a sound")


class Prey:
    def escape(self):
        print("This animal tries to escape")


class Predator:
    def hunt(self):
        print("This animal is hunting")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"{self.name} is a {self.breed}")

    def speak(self):
        print("Dog barks")


class Fish(Animal, Prey, Predator):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Fish cannot bark but makes bubbles")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


def animal_sound(animal):
    animal.speak()


dog = Dog("Tommy", "Bulldog")
fish = Fish("Nemo")
cat = Cat("Kitty")

print("\n--- Actions ---")

fish.hunt()
fish.escape()

print("\n--- Polymorphism ---")

animal_sound(dog)
animal_sound(cat)
animal_sound(fish)