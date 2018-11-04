import pprint

employees={}
num = int(input("Number of employees's data to be added : "))
for i in range(0,num):
    empId  = input("EmpID of employee : ")
    fname = input("First Name of employee : ")
    lname = input("last Name of employee : ")
    salary = input("Salary of employee : ")
    nickname = input("nickName of employee : ")
    employees[empId] = {'Name' : fname+" "+lname, 'Salary': salary, 'Nick' : nickname}
print(employees)
pprint.pprint(employees)
    
    
