"""Python Program to Reverse a Given Number"""
n = input("Enter the number > ")
num=""
lst = list(n)
lst.reverse()
num ="".join(lst)

print("Reversed Num ",num )