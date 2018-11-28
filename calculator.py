def operation(ops,x,y):
    if(ops==1):
        return x+y
    elif(ops==2):
        return x-y
    elif(ops==3):
        return x*y
    elif(ops==4):
        return x/y
    elif(ops==5):
        return x%y
    elif(ops==6):
        return x*x
    else:
        return 0


print("Welcome to simple calculator program")
print("you can perform following operations : "'\n',
      '\t'"1. Addition"'\n',
      '\t'"2. Subtraction"'\n',
      '\t'"3. Multiplication"'\n',
      '\t'"4. Division"'\n',
      '\t'"5. Modulus",'\n'
      '\t'"6. Squaring")
ops=int(input("Enter the operation you want to perform : "))
if(ops==6):
    x=float(input("Enter the Num : "))
    y=x
else:
    x=float(input("Enter the First Num : "))
    y=float(input("Enter the Second Num : "))

Result = operation(ops,x,y)
print (" Result of your operation is : ", Result)

