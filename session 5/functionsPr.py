# two type of functions : built in functions and user define functions 

# built functions are alredy define in python 
print("Here is built in functions")

# user define functions
def func():
    print( "somethinggg")
    
func()
    

def square(a):
    print("Square function is called")
    return a*a

output=square(10)
print(output)

# if function doesn't return anything then it return the NONE


# keyword argument in function

def func_key(first, second, third):
    print(f"First : {first}")
    print(f"second : {second}")
    print(f"third : {third}")

func_key(first=10, second=20, third=30)




# default arguments 
print("--default arguments--")
def def_fun(first, second=0, third=1):
    print(f"First : {first}")
    print(f"second : {second}")
    print(f"third : {third}")

def_fun(first=10, third=30)








def fun(n):
    print("Calling function")
    return 10*n

fun(5)
print(fun(5))
print(fun('Argument'))
print(fun(5*10))
print(fun(1+2j))
print(fun('1j'))
print(fun(1j))


# *args
#args pass all the arguments as tuple 
def aDef(*args):
    print("This is function with *args")
    print(f"type of args {type(args)}") # type of args is tuple
    for a in args:
        print(a)

aDef(1,"2",{3,4},[5,6],{7:40},(8,9))


# *args
#args pass all the arguments as dictonary 
def kDef(**kwargs):
    print("This is function with ** kwargs")
    print(f"type of args {type(kwargs)}") # type of args is dictonary
    for k,v in kwargs.items():
        print(f"{k} = {v}")


kDef(first='a', second=1, third=(2, 3,), fourth=[2, 'b'], fifth=2.14, sixth={1:"one",2:"two"})




# Lambda functions aka Anonymous function 


square_num = lambda x : x*x 


print("----print the lambda function---")
print(square_num(5))


# use lambda function as a argument in another function such as sort


user = [("name", 'ajay'), ("age", 22), ("profession", 'developer')]

user.sort() # this sort according to alphabat

print(user)

print("----lambda functions------")

user = [("hobby", "photography"), ("profession", 'developer'),("name", 'ajay')]

user.sort(key=lambda usr: usr[1]) 
# this lambda function sort the value  of each iterations

print(user)
