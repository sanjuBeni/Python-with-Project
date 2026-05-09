
"""
    Dunder Methods:- Dunder methods are special method that change the behavior of the object. These methods are start and end with double underscores. 

    __init__ is also a Dunder methods
    some useful Dunder Methods
        __str__
        __eq__
        __add__
        ,etc 

"""
# class EmployeeDetail:
#     def __init__(self, emp_id, name, mobile, email):
#         self.emp_id = emp_id
#         self.name = name
#         self.mobile = mobile
#         self.email = email

#     def __str__(self):
#         return f"Employee ID: {self.emp_id}\nEmployee Name: {self.name}\nMobile: {self.mobile}\nEmail:{self.email}"


# obj = EmployeeDetail("ABC123", "Jack", "9876098765", email="abc@g.com")
# print(obj)



# Add Two object
class MyNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num


obj1 = MyNumber(10)
obj2 = MyNumber(90)
print(obj1 + obj2)
