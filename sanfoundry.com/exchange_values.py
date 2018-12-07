"""Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable"""
a = int(input("Enter First num >"))
b = int(input("Enter Second num >"))

a=a+b
b=a-b
a=a-b

print("A = ",a,"B = ",b )