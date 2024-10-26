from string import Template


#String format method

# 1 .format() method

print("Name of popular programming laguages {} ".format("python"))

#give index for modify order of method
print("Name of popular programming laguages {1} {0} ".format("python", "java"))

# use  list in format
list1=['a','b','c']
print("list of items {}".format(list1))

# use variables 
num1= 4
num2=3
print("use variable here, num1 :  {} num2 : {}".format(num1, num2))


# F string 

name="Ajay"
print(f"My name is {name}")
listOfLan= ['python', 'JavaScript']
print(f"Hello, i am learning this programming languages {listOfLan}")

# if data is dynamic then we have to use .format() function, otherwise we have to use f string 



# template method

str1= Template("Hi, there this is number $num1")
print(str1.substitute(num1=num1)) # substitute method add variable 


# conditional statement 
condition=False
if condition :
    print("this is if block")
else:
    print("this is else block ")

sum = 10

if sum<50:
    print("below the average")
elif sum>50 and sum<80:
    print("moderate score")
else:
    print("excellent score")
    
    

