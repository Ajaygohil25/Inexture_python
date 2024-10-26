# immutable objects in python


a =100
print(a, "Id of :", id(a))

b = 100
print(b, "Id of :", id(b)) 

# a and b referring to same memory point

# if we change value of a then it refer to another memory address but B remain at the same memory referance
print("------after changing a : ")
a=5
print(a, "Id of :", id(a))

b = 100
print(b, "Id of :", id(b)) 

# concept of garbage collector --> Doubt 

# mutable objects

list1 = [12,34,56,78,90]

list2 = [12,34,56,78,90]
print(list1, "List 1 It's  memory location ", id(list1))
print(list2, "List 2 It's memory location ", id(list2))

# although value is same in both  of the list still they are 
#refering to different memory locations 

list1.append(89)

print(list1, "List 1 after appending  It's  memory location ", id(list1))


# with "=" assignment operator both lists are refer to same memory locations 

list1 = list2
print("--- after assignment---")
print(list1, "List 1 It's  memory location ", id(list1))
print(list2, "List 2 It's memory location ", id(list2))

# change in anyone of it refer both of the list 
list1.append(98)

print(list1)
print(list2)

list2.append(88)

print(list1)
print(list2)