class Dog():        #Creating the Dog class
    def __init__(self, name, age): #Self is the dog itself, it passes automatically
        self.name = name    #We just need to pass the other 2 parameters
        self.age = age

    def sit(self):          #Creating 2 Methods for dog
        print(self.name.title() + " is now sitting.")
    def run(self):
        print(self.name.title() + "is now running.")

my_dog = Dog("Huskey", 3)
my_dog.sit()
my_dog.run()
my_dog.food = "My dog eats cat food. Dunno why"
print(my_dog.food)

class Dog(object):      #This new Class overrides the Previous one
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "Dog name: " + self.name
my_dog = Dog("Caramelo")
print(my_dog)
