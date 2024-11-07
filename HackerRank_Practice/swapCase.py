
def swap_case(string):
    list_str= list(string)
    for i in range(len(list_str)):
        if str(list_str[i]).isupper():
            # print(list_str[i],end= ' ')
            list_str[i] = str(list_str[i]).lower()
        elif str(list_str[i]).islower():
            # print(list_str[i], end= ' ')
            list_str[i] = str(list_str[i]).upper()
        # else:
        output= ''.join(list_str)        
    return output


string = "Www.HackerRank.Com"

print("output is : ",swap_case(string))