# for loop 
# for loop in list 

list1= [2,4,5,6]

for i in range(len(list1)):
    print(i, end='\t')


l = [i for i in range(len(list1)) if i==3]
print("\nprint list comprehention : ",l)

# for loop over tuple

tuple1 = (1,3,6)
# tuple can not comprehens... Doubt...
print("tuple loop")
for tp in range(len(tuple1)):
    print(tp)
t = (i for i in range(len(tuple1)) if i==3)
print("\nprint tuple comprehention : ",t)
set1= {3,4,5,4,60}
print(set1)


# for loop in dictonary

dict1 ={  
    "name":"ajay",
    "age" : 22,
    "Study" : "MSc IT"
}

print("\n Key of dictionary through loop")
for key in dict1:
    print(key, end='\t')

print("\n value of dictionary through loop")
for values in dict1.values():
    print(values, end='\t')


# access key and value pair
for key,val in dict1.items():
    print(f"Key = {key} and value = {val}")


# iterate over range

print("Range function in loop")

for i in range(0,10):
    print(i, end=' ')


#else with loops 

print("for with else ")
for i in range(0,10):
    if i>5:
        break
    print(i, end=' ')
else:
    print("execution completed ")    


flag=True
n=0
while n<10:
    print(f"this condition is true {n} time")
    n+=1
    if  n>5:
        break
else:
   print("execution completed ")    
    



# concept of nested loop and breaking nested loop

# nested loop working !!

# breaking the  nested loop 
# way 1 using flags
flag=True
for i in range(1,10):
    for j in range(i+1, 10):
        if j>5:
            flag=False
            break
        print(f"i {i} j {j}")
    if flag==False:
        break    
    


# complex one :
# breaking the nested loops using flags 

flg1=False
flg2=False


print("breaking 3 loops using flags")
for i in range(7):
    for j in range(7):
        for k in range(7):
            print(f"I {i} j {j} k {k}")
            if k>3:
                flg1=True
                break
        if flg1:
            flg2=True
            break
    if flg1 or flg2:
        break

# break the nested loop using try and catch exception handling

print("Trying try and catch exception handling")
class OutOfLoop(Exception):
    pass

for i in range(10):
    try:
        for j in range(10):
            if j>5:
                raise OutOfLoop
            print(f"I {i} j {j}")
    except OutOfLoop:
        break
        



# using functions 
print("Using the loops to break the functions")
def check_loops():
    while True:
        for n in range(10):
            if n>5:
                return
            print(f"n {n}")
check_loops()    



    



