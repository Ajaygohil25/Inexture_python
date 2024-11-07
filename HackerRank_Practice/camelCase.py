def case(string):
    val = string.split(" ")
    output_str=""
    for i in val:
        for j in range(len(i)):
            if j==0:
                temp=i[0]
                output_str+=temp.upper()
            else:
                output_str+=i[j]
        output_str+=" "
    return output_str
string="ajay gohil"
print(case(string))