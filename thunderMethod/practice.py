# thunder method can't explicitly invoked it, it only invoked when user perform certain actions

print(dir(int)) # list out all thunder methods of python




def __add__():
    print ("hi i am doing something")

print(6+4)
__add__()

class Subject:

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


obj = Subject('Maths', 'Science')
# op= obj.__init__('Maths', 'Science')
print(obj.attr1)  
print(obj.attr2) 
print("output ",op)