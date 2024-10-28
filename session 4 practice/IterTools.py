# Iter tools for perform operations on dataset

# Merging and Splitting Iterators 
# for join two large iterable 
from itertools import chain

numbers=[1,4,6,9]
chars=['a', 'b','c','d']

chain_val = chain(numbers,chars)

for i in chain_val:
    print(i,end= ' ')

# chain from  unknown iterable chain 

def make_chain():
    num_odd_50=[]
    num_even_50= []
    for num in range(100):
        if num%2==0 and num<50:
            num_even_50.append(num)
        elif num%2!=0 and num>50:
            num_odd_50.append(num)
    
    yield num_even_50
    yield num_odd_50

output= make_chain()

print(f"\n Type of object {type(output)}")

print(next(output))
print(next(output))


        
for i in chain.from_iterable(make_chain()):
    print(i, end=' ')

# .from_iterable() will give me list of values as a chain 



# zip()

num= [1,2,4]
characterss= ['a','f','k','l']

zip_iteraters = zip(num, characterss)

for i in zip_iteraters:
    print("\n",i)

    