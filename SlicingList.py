#Print The Galaxy's Guide to the Hitchhiker
book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print (booklist)
tempList = booklist[0:3]   #['T', 'h', 'e']
tempList2 = booklist[-6:]
i=0
for char in tempList:
    for j in range (i,3):
        booklist.insert(j,char)
        break
    i=i+1
i=3
for char in tempList2:
    for j in range (i,9):
        booklist.insert(j,char)
        break
    i=i+1
for i in range (10):
    booklist.pop()
booklist.insert(3,booklist.pop())
for char in booklist:
    for j in range (11):
        booklist.insert(10,booklist.pop())
        break
booklist.insert(10,booklist.pop())
booklist.insert(21," ")
print (booklist)
phrase = ' '.join(booklist)
print (phrase)
