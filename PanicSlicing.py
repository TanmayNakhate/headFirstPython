#Print On taP 
phrase = "Don't Panic!"
plist = list(phrase)
print(phrase)

new_phrase = ''.join(plist[1:3])
print(new_phrase)
new_phrase = new_phrase+''.join([plist[5],plist[4],plist[7],plist[6]])
print(plist)
print(new_phrase)
