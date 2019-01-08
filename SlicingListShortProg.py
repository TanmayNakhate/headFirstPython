#Print The Galaxy's Guide to the Hitchhiker
from builtins import print

book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print (booklist)
newList = ''.join(booklist[-10:])+''.join(booklist[14:26])+''.join(booklist[0:14]) 
print (newList)



a=[1,2,3,4,5,6,7,8,9]
print(a[::-1])
print(a[-1:4:2])


l = [0,1,2,3,4,5,6,7,8,9]
print("#######################")
print(l[7:2:-1])  #[7, 6, 5, 4, 3]
print( l[-3:2:-1])  #[7, 6, 5, 4, 3]
print(l[-3:-8:-1])   #[7, 6, 5, 4, 3]
print(l[-3:2:1])  #[]
print(l[7:-8:-1])   #[7, 6, 5, 4, 3]