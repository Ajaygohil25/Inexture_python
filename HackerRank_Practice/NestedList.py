# name of student and their grade store it on list of list 
# records= [["a", 30.0], ["b",20.0]]

# print("print number of students : ")
n = int(input())
student=[]
for i in range(n):
    name =input()
    grade=float(input())
    student.append([name,grade])

list_grade = list(set([student[x][1] for x in range(len(student[1]))]))
s_low = list_grade[1] 
s_name=[]
for i in range(len(student)):
    if student[i][1] ==  s_low:
        s_name.append(student[i][0])
s_name.sort()
print(s_name)
  









