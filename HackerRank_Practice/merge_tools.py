# Merge the Tools!

# divide substring based on n/k  
# string = "AABCAAADA"
# k=3

def merge_the_tools(string, k):
    n=len(string)
    count=0
    substr =""
    for i in range(n):
        if count==k:
            count=0
            temp=""
            substr = list(substr)
            for j in substr:
                if j not in temp:
                    temp+=j
            print(temp)
            substr =""
        substr+=string[i]
        count+=1
    if count==k:
        temp=""
        substr = list(substr)
        for j in substr:
            if j not in temp:
                temp+=j
        print(temp)
        

   

string = input("Enter String : ")
k= int(input("Enter value of k  :"))

merge_the_tools(string, k)