import re

list = ["guru99 get","guru99 give", "guru Selenium", "guru 99"]
xx = "guru99.education is fun"
abc = 'guru99@google.com,careerguru99@hotmail.com, users@gmail.com'

print (re.findall(r"\d+",xx))

for element in list:
    z = re.match("(g\w+)\W(\d)",element)
    if z:
        print (z.groups())

emails = re.findall(r'[\w+]+@[\w+\.]+',abc)
for mail in emails:
    print (emails)