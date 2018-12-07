"""Python Program to Calculate the Average of Numbers in a Given List"""

count = int(input("Enter the count of numbers you want to add in list > "))
list=[]

for i in range(0,count):
    num = int(input("Enter the numbers in list > "))
    list.append(num)

print("you entered these nums in list = ",list)
print("Avg of nums in list = ",sum(list)/len(list))

