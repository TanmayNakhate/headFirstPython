from prettytable import PrettyTable
from os import listdir
from os.path import isfile,join

mypath = 'C:\\tmp\\excel\\'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("Only Files = ",onlyfiles)

for i in range(0,len(onlyfiles)):
    csv_file = open(mypath+onlyfiles[i])
    csv_file = csv_file.readlines()
    final_list=[]

for i in csv_file:
    print("i = ",i)
    final_list.append(i.strip())
print(final_list)

line_1 = final_list[0].split(',')


print("line_1[0]==",line_1[0])
print("line_1[1]==",line_1[1])

x= PrettyTable(['Test_Name','Status'])

for a in range(0,len(line_1)):
    print("line_1[a]==", line_1[a])
    print("line_1[a]==", line_1[a+1])
    x.add_row([line_1[a],line_1[a+1]])
    break;

html_code = x.get_html_string()
html_file = open('C:\\tmp\\Result.html','w')
html_file = html_file.write(html_code)
print("html file = ",html_file)

#print("https: // www.youtube.com / watch?v = KDB892oS7pk")