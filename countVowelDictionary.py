word = input("Write word to find occurance : ")
vowel = ["a","e","i","o","u"]
found = {}
print(found)
for char in word:
    if char in vowel:
        found.setdefault(char,0)
        found[char]+=1
for k in sorted(found):
    print(k, 'was found',found[k],'times',"using sorted method")
print("----------------------")
for k,v in sorted(found.items()):
    print(k, 'was found',v,'times',"using sorted items method")
print(found)
