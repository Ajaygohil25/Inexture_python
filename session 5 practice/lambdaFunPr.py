# practice of lambda function


# 1) 
# Write a Python program to create a lambda function that adds 
# 15 to a given number passed in as an argument, also create 
# a lambda function that multiplies argument x with argument y and prints the result.

add_num =  lambda x: x+15

print(add_num(10))

multiply_num =lambda x,y: x*y
print(multiply_num(2,3))

# 2). Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.



def fun_cal(num):
    return lambda x: x*num


result =fun_cal(2) # here we pass argument, lambda function store in result 

print(f"this is call of lambda function : {result(10)}") # this will give output because we have call lambda function

