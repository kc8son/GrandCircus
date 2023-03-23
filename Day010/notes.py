class Animal:
    def __init__(self, n):
        self.name = n
    def eat(self):
        print("Yummy, thanks for the food!")
    def speak(self):
        print("Hello fellow earthlings.")


# class Pet(Animal):
# ---
# ---
#
# class Cat(Animal, Pet):
#   in __init__ we can use multiple arguments to initialize "member variables"

class Cat(Animal):
    def __init__(self, n):
        Animal.__init__(self, n)
    def clean_litter(self):
        print("I am cleaning my own litter box.")
    def speak(self):
        print("Meow...")

class Dog(Animal):
    def vspeak(self):
        print("Woof!")
    def chase_ball(self):
        print("I am chasing the ball!")



a1 = Animal("generica animal")
a1.eat()
a1.speak()

fluffy = Cat("Fluffy cat")
fluffy.eat()
fluffy.speak()
print(fluffy.name)