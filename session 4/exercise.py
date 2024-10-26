# Given a list of values inputs and a positive integer n, 
# write a function that splits inputs into groups of length n. For simplicity, 
# assume that the length of the input list is divisible by n. 
# For example, if inputs = [1, 2, 3, 4, 5, 6] and n = 2, your function should return [(1, 2), (3, 4), (5, 6)].

from itertools import zip_longest
 
def group_lists(list1, n):
    iters = [iter(list1)] *n # it will give 2 iter objects 
    return zip(*iters)

list1 = [2,3,5,7,10]
output= group_lists(list1,2)

for i in output:
    print(i)


# same thing we want to do the code, and want a tuple that have a single value

print("output for the zip longest")
 
list1 = [1,2,3,4,5,6,7,8,9,10]
def group_lists(list1, n):
    iters = [iter(list1)] *n # it will give 2 iter objects 
    return zip_longest(*iters, fillvalue=0)


output= group_lists(list1,4)
for i in output:
    print(i)


