
class Encapsulation:
    # public attributes and methods 
    name = "Under stand Encapsulation"
    def public_method(self):
        print("This method is public")

    # Protected attributes and methods
    _xyz = "Protected variable"

    def _protectedMethod(self):
        print("This is protected method.")

    
    # Private attributes and methods
    __DB_NAME = "DATABASE NAME"

    def __private_method(self):
        print("This is private method")


obj = Encapsulation()
print(obj.name)
obj.public_method()
print(obj._xyz)
obj._protectedMethod()
