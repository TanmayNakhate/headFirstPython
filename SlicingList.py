#Print The Galaxy Guide to the Hitchhiker's
book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print (booklist)
tempList = booklist[0:3]   #['T', 'h', 'e']
print (tempList)
for char in tempList:
    for j in range (0,3):
        booklist.insert(j,char)
        break
#booklist.insert(0,tempList)
print (booklist)
