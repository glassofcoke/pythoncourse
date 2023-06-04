class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("MEOOOOWWW!")

class Bird(Animal):
    def sound(self):
        print("pew pew pew")
class Dog(Animal):
    def sound(self):
        print("ARGGHH RAULF RAULF RAULF")

caramelo = Dog()
jessica =  Cat()
pinto = Bird()
my_pets =[caramelo, jessica, pinto]

for x in my_pets:
    x.sound()

print(isinstance(caramelo,Dog))
print(isinstance(jessica,Animal))