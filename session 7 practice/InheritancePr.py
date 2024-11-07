class ParentClass:
    def method_a1(self):
        print("This is a method of parent class")
    def method_b(self):
        print("This is b method of parent class")
        # self.method_a() # this will call method of child class because it has a higher priority 

class ChildClass(ParentClass):
    def method_a1(self):
        print("This is a method of child class")
        # self.method_b()

class ChildClass2():
    def method_a(self):
        print("This is a method of child 2 class")
        # self.method_b()

childObj =ChildClass()

# childObj.method_b()
 

 # multilevel inheritance

class multipleClass(ChildClass, ChildClass2):
    # super().method_b()
    def __init__(self):
        pass
        # super().method_b()
m = multipleClass()
m.method_a()

# class multipleClass(ParentClass,ChildClass):
#     # super().method_b()
#     def __init__(self):
#         pass
#         # super().method_b()
# m = multipleClass()
# m.method_a()



