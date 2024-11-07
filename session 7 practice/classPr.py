class CustomClass:
    name =" ajay"
    def __init__(self, age, profession):
        self.a= age
        self.p= profession

    
    def __str__(self):
        return f"Hi, there I am {self.name}. My age is {self.a} and I have a profession of {self.p}"
        
    # def p(self):
    #     var =45

         


c = CustomClass(22,"programmer")
c.hobby = "photography" # it will create object at instance level 
print(c)
print()
print(c.hobby)

c1= CustomClass(23, "Tester")
print(c1)
# print(c1.hobby) # AttributeError: 'CustomClass' object has no attribute 'hobby'
# hobby attribute only belongs to "c" instance 


# if function declare outside of class and we want to use inside the class or we want to intialize that method inside class that could be possible 

def func(self, a,b):
    return a*b

class Pr:
    fun= func

p= Pr()

output=p.fun(a=30,b=40)
print(f"this is output : {output}")

# def __init__():
#     print("hey")
    
# __init__()



# creating a private variables in python 

# in python there is no concecpt like private variable 
class Private:
    def __init__(self):
        self._var="private" # _var "_" is just a convention that it can be consider as private variable 


    def _privateFun(self):
        print("this is a private method")

p = Private()

print("accessing : ", p._var)
p._privateFun()

# concept of mangling 

class mangClass:
    # __var ="otherObj"
    def __init__(self):
        self.__var="MangObj"

m= mangClass()
print("this is calling mangling var", m._mangClass__var)



# Python code to illustrate how mangling works 
# With method overriding 

class Map: 
	def __init__(self): 
		self.__geek() 
		
	def geek(self): 
		print("In parent class") 
          
	__geek = geek	 
	
class MapSubclass(Map): 
		
	def geek(self):		 
		print("In Child class") 
		
obj = MapSubclass() 
obj.geek() 



class YoungTalent:
    
    abilities = ['Super power', 'I can fly in air']
    power = 100
    
    def __init__(self, name, email, god_father):
        self.name = name
        self.email = email
        self.god_father = god_father
        
    def add_ability(self, ability):
        self.abilities.append(ability)
#         self.abilities = [ability]

    def change_power(self, power):
        self.power = power
    @classmethod # class method will change at the class level for immutable sequence s
    def change_mypower(cls, power):
         cls.power=power
    
    # @classmethod
    # def change_myAbilities(cls, abilities):
    #      cls.abilities.append(abilities)
         
         
    def __str__(self):
         return f"name {self.name} abilities {self.abilities} power {self.power}"


y = YoungTalent("Spider man","iam@spidy.com","Iron man")
z= YoungTalent("Thor","thunder@thor.com","Ascgard")


print(y)
print(z)

# z.add_ability("I have power of thunder")
z.change_myAbilities("I have power of thunder") 

z.change_mypower(1000)
print(y)
print(z)