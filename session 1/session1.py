a = None

print("this is a ", a, "type is ", type(a))
print("this is a ", a, "type is ", id(a))

a = "Coder"

# id() returns a memory location of a object 
# None type is Immutable and when reassign variables then they store in different locations
print("this is a ", a, "type is ", type(a))
print("this is a ", a, "type is ", id(a)) 

# data types
# String immutable

str1 = "Python developers"
if "Python" in str1:
    print("true")
 
print("bofore", str1) 
# str1[9] = "k"
# print(str1)

#tuple 

tuple1= ("Python developers", "java developers")
print(tuple1)

tuple2 =("QA", "Tester")
# for join the tuple
tuple3 = tuple1  + tuple1
print(tuple3)

# list and list operations 

a = ["a", "b", "c"]

print("a:  ", a)
print("id of a ", id(a))

b =[1,2 ,3,4] 
# .extend() for join the list together
a.extend(b)
print("a after extend:  ", a)
print("id of a ", id(a))
c= [True,False]
a= a+c

print("a after extend using  :  ", a)
print("id of a ", id(a))

# insert elemenent 

a.insert(2, "kbc")
print("a after insert", a)

output =  a.index("kbc")
print("output ", output)
# a.sort()
# print("a after sort", a)

a.remove("a")
print("a after remove", a)

del a[0]
print("a using index ", a)

# list shorthand 


#----------------------------

