# list comprehenstion  x,y,z sum should not equal to n 

x = int(input())  # 2 --. 0,1,2
y = int(input())  # 2.. 0,1,2
z = int(input()) # 3 .. 0,1,2,3
n = int(input())

list1 = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n]
print("is runnig")
print(list1)