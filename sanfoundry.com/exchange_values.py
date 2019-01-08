"""Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable"""
a = int(input("Enter First num >"))
b = int(input("Enter Second num >"))

a=a+b
b=a-b
a=a-b

print("A = ",a,"B = ",b )

n=int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()