
class Animal:
    def sound(self):
        print("Animal make sound")


class Cat(Animal):
    def sound(self):
        print("Cat meows")
        # Parent class overriding method call
        super().sound()

class Dog(Animal):
    def sound(self):
        print("Dog barks")

c = Cat()
c.sound()

d = Dog()
d.sound()