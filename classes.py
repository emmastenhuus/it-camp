class Person:
    def __init__(self, nm, h = 180):
        print("Constucting:", nm)
        self.name = nm
        self.height = h
        print("Done")

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()
print(john.name)


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
