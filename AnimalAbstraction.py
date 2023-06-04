from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eats_grass(self):
        pass

    def is_animal(self):
        return True

class Cat(Animal):
    def __init__(self):
        print("The cat")
    #OVERRIDING ABSTRACT METHOD
    def eats_grass(self):
        return False

meow = Cat()
print(meow.is_animal())
print(meow.eats_grass())