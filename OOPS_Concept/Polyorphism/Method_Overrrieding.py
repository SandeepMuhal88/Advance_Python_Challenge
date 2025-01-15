class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def speak(self):
        print("Dog Barking")

class cat(Animal):
    def speak(self):
        print("Cat Meowing")

class Lion(Animal):
    def speak(self):
        print("Lion Roar")

animals=[Dog(),cat(),Lion()]
for i in animals:
    i.speak()
