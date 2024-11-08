# import decoratorsPr
name="Python the best"

def change_lan():
    global name  #but this  one will change both
    name="Java the secure one" # only change inside function
    print("inside fun",id(name))
    return name 

output= change_lan()
print(output) 
print("outside fun",id(name))
print(name)


# print(locals())  # locals of outer scope

# Use of nonlocal keyword

x = "a"
def outer():
    x = "b"
    def inner():
        #nonlocal x # with use of nonlocal x it will change value of outer function's x 
        global x # it will change value of global x  with is in global score
        x = "c"
        print("from inner:", x)

    inner()
    print("from outer:", x)

outer()
print("globally:", x)