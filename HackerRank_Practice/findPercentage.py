if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        print("score",scores)
        student_marks[name] = scores
        
    query_name = input()
    if query_name in student_marks.keys():
        list1= student_marks[query_name]
        total=0
        for i in range(len(list1)):
            total+=list1[i]
        total=total/len(list1)
        print("{:.2f}".format(total))

        