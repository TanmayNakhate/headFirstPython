import re

s = '“Where have you been hiding out”, asked the King.“I’m afraid all the heads have been given out, and there is not a single one left for you!”'
#with open("G:\Learning_Curves\headFirstPython\headFirstPython\story.txt",'r') as f:
#    for line in f:
#        print(line)
print(s)
s = re.sub(r'[^\w\s]','',s)


#pattern = re.compile(r"*?(\"\,\.\')")
print(s)

