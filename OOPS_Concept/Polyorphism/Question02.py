# Duck typing
class m1:
    def info(self):
        print("I am from M1 class")

class m2:
    def info(self):
        print("I am from M2 class")

class m3:
    def info(self):
        print("I am from M3 class")


def function(*a):
    for i in a:
        obj=i()
        obj.info()

function(m1,m2,m3)

class Duck:
    def quack(self):
        print("Quack, quack!")

    def swim(self):
        print("I can swim!")

class Dog:
    def quack(self):
        print("I can mimic a duck: Quack, quack!")

    def swim(self):
        print("I can swim too!")

def act_like_a_duck(duck):
    duck.quack()
    duck.swim()

# Both Duck and Dog can "act_like_a_duck"
d = Duck()
dog = Dog()

act_like_a_duck(d)
# Output:
# Quack, quack!
# I can swim!

act_like_a_duck(dog)
# Output:
# I can mimic a duck: Quack, quack!
# I can swim too!
