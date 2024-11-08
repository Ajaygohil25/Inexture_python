def func1():
    var="python"
    def func2():
        text="web development"
        print(f"i am accessing the var: {var}") # it can access the variable of outer pr parent function
    func2()
    print("Hey i am outer function ")
    

func1()


# simple decorator

def SayHi():
    return "Hi I am Ajay"

def greet(SayHi):
    return SayHi

fun_decorator = greet(SayHi)
print(fun_decorator())

# use @ for decorator
def greet(SayHi):
    return SayHi

@greet  # same as fun_decorator = greet(SayHi)
def SayHi():
    return "Hi I am Ajay"

print(SayHi())


# Generator that modify the value of existing content of function 

def Modifier(function): # this function modify the string and add the content into existing string 
    def wrapper():
        content = function()
        return_content= content.upper() + " Oh, You are champ !"
        return return_content # wrapper function is returning the modified string
    return wrapper # Modifier return Wrapper function 

@Modifier
def intro():
    return "hi i am python developer. I am learning a python and I love to explore it !!"

print(intro()) 



# # applying multiple modifier 
def StrictDecorator(Score):
    print("I am Strict outer")
    def Wrapper(*args):
        print("I am Strict Checking decorator ")
        S_score= Score()  # it's actually wrapper  function of chill decorator 
        if(S_score<60):
            print(f"That's not enough, work more harder, {S_score}")
            return "i am done"
        else:
            print(f"Good!, just stay down to earth! {S_score}")
            return "i am done"
    return Wrapper

def ChillDecorator(Score):
    print("I am child outer")
    def Wrapper(*args):
        print("I am chill Checking decorator ")
        score= Score() # it;s calling score func
        if(score<60):
            print(f"That's okay, focus on learning, {score}")
            return score
        else:
            print(f"Oh! That's great champ  {score}")
            return score
    return Wrapper
        


@StrictDecorator 
@ChillDecorator # this will retur the wrapper of chill
def Score():
    s=int(input("Enter your score :"))
    return s


# learn about the execution order of decorators  above code same is this
# out1 = ChillDecorator(Score) #  out 1 is actually wrapper function of childDecorator

# out2= StrictDecorator(out1) #  we are passing out1 in a way wrapper function of childDecorator as a argument in Strict



# print(type(s))
print(Score())




