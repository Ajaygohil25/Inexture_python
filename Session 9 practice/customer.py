# import Admin as ad

# ad.workMode() # this will give circular import problem 
list_customer =[]
def add_customer():
    name=input("Enter name : ")
    salary= int(input("enter salary : "))
    dict1={}
    dict1["name"]=name
    dict1["salary"]=salary
    list_customer.append(dict1)
    return list_customer


def print_allCustomer():
    if len(list_customer)==0:
        add_customer()
        print(list_customer)
    else:
        print(list_customer)

print_allCustomer()

    
# print global 
# import pprint
# pprint.pprint(globals())
    
