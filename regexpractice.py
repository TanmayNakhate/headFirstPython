import re

def checkstring(str):
    pass






text_to_search='''1)“Hey… Avantika come have a seat. 2)”“Thank You :Chetan!”, she replied and I ordered two cups of coffee.
3)“So Avantika, what kind of characters you want me to introduce in my next book.”, I asked her"'''

txt = text_to_search.split(" ")
print(txt)
pattern = re.compile(r'[^a-zA-Z0-9]')
for i in txt:
    matches = pattern.finditer(i)
    print(matches)

for match in matches:
    print(match)
