word = input("Please enter a word : ")
wrdList = list(word)
noDuplis=[]
for char in wrdList:
    print (char)
    if char not in noDuplis:
        noDuplis.append(char)
print (noDuplis)
        
