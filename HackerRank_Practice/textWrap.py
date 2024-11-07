def wrap(string, max_width):
    count=0
    l=len(string[:-1])
    # print(l)
    
    str1=""
    for i in range(0,len(string)):
        if i==l:
            str1+=string[i]
            return str1
        if count==max_width:
            print(end='\n')
            count=0 
        count+=1
        print(string[i],end='')  