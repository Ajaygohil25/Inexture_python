# comprehension is used for creaing iterable from
# othe iterable 

values = [2,3,6,7,10]
result = [n*10 for n in values]

print("this is list : ",values )
print("this is a result ",result)   

# conditions in list comprehensions
# 2 type of conditions: 1> filter item, 2> change items


#1 filter  items 

filter1 = [n for n in values if n%2==0]

print("fiilter 1 value ", filter1)

filter2 = [n if n%2==0 else 0 for n in values]

print("fiilter 2 value ", filter2) 

# using change item method list size remain same as original list


# try to comprehension the tuple, because it has mutable property

tuple1 = (1,2,4,4,2,1)

tupleFilter = (n for n in tuple1 if n>3)

print("Tuple filter ", tupleFilter)

# However it may possible using  temp() --> Doubt

tuple1 = (1,2,4,4,2,1)

tupleFilter = tuple (n for n in tuple1 if n>3)

print("Tuple filter ", tupleFilter)

# comprehension in set and dictonary
# set comprehension stores only unique values as property of set

sentence = "Hey there i am learning the python"

vowels = "aeiou"

vowels_words=  {char for char in sentence if char in vowels}

print(f"this is sentense {sentence} and this is words {vowels_words}")



# dictonary 
# in dictonary need to give ":" for generate key value pair
dictComp ={num: num*2 for num in values }

print("this is dictonary comprehansion ", dictComp)

