from collections import Counter, ChainMap

# counter is a sub-class of dictonary 
list1= [3,4,6,7,9,3,6,8]

items =Counter(list1)

print(items)  # print ccunter 

print("elements : ",list(items.elements()))



# ordered dic

dictionary = {1:"a",2:"b", 4:"c", 6:"t"}

print(dictionary)

# chain map combine many dictionarys into one units


dict1 ={"a": 1, "b":3, "c": 4, "t":4}
dict2 ={"d": 3, "e":4, "f": 5}
dict3 ={"a": 1, "k":7, "c": 8}


chain = ChainMap(dict1, dict2, dict3)

print(type(chain))
print(chain.maps) # return one list that combine all three dictonary

print(list(chain.keys())) # return  all unique keys 
print(list(chain.values())) 


# update the value of chain 
chain["ab"]=5 # it will add the element in the very fist list
print("after update" ,chain.maps)
