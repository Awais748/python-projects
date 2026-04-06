class Animal:
    total_animals = 0   

    def __init__(self, name):
        self.name = name
        Animal.total_animals += 1


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Bird(Animal):
    pass


dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")
bird1 = Bird("Tweety")

dog2 = Dog("Max")

print(dog1.name)
print(cat1.name)
print(bird1.name)

print("Total Animals:", Animal.total_animals)