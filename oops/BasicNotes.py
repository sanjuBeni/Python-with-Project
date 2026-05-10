from StaticMethodClass import StaticMethodClass

class BasicNotes:
    # Class attributes
    PI = 3.14
    DATABASE_NAME = "MY_DATABASE"

    def __init__(self, name, email, age):
        # Instance Attribute
        self.name = name
        self.email = email
        self.age = age


    # Instance Method
    def instance_method(self):
        print(f"{'Student Name':20} {'Email':30} {'Age':20}")
        print(f"{self.name[:20]:20} {self.email:30} {self.age}")

    #class method
    @classmethod
    def class_method(cls):
        print("This is class method")
        print(f"Static method call: {StaticMethodClass.km_to_meter(100)}")
        print(cls.PI, cls.DATABASE_NAME)

    #Static Method
    @staticmethod
    def static_method(x, y):
        return x+y



s1 = BasicNotes('Student 1', 's@g.com', 20)
s1.instance_method()
BasicNotes.class_method()