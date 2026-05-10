from Parent import Class_Main
from Child_1 import Child_1

# Hierarchical Inheritance
class Child_2(Child_1):
    pass

o = Child_2('naxyz')
o.child_1_data()
o.print_name()