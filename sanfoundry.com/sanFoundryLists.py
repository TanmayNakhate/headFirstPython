import random
import os


class listsProg:
    """Python Program to Find the Largest Number in a List"""
    def largeList(self,lst):
        print("Largest Number in list : ",max(lst))

    """Python Program to Find the Second Largest Number in a List"""
    def secondLargest(self,lst):
        lst.sort()
        print("Second Largest Number in list :",lst[-2])

    """Python Program to Put Even and Odd elements in a List into Two Different Lists"""
    def evenodd(self,lst):
        evenList=[]
        oddList=[]
        for i in lst:
            if i%2==0:
                evenList.append(i)
            else:
                oddList.append(i)
        print("List of Even elements in given list",evenList,"\n"
              "List of Even elements in given list",oddList)

    """Python Program to Merge Two Lists and Sort it"""
    def sortmerge(self,lst):
        words = ['v','b','a','f','s','f','g','w']
        print("List to merger :",lst)
        words.sort()
        lst.sort()
        words.extend(lst)
        print("extend() words List with lst : ",words)   #['a', 'b', 'f', 'f', 'g', 's', 'v', 'w', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        words.append(lst)
        print("Append() words List with lst : ",words)   #['a', 'b', 'f', 'f', 'g', 's', 'v', 'w', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
        #Sort() and Sorted() methonds cannot be used since both lists are of diff types.

    """Python Program to Sort the List According to the Second Element in Sublist"""
    def sortbysecondelem(self):
        words = [['a',12],['d',123],['b',13],['q',5],['b',45]]
        for i in range(0,len(words)):
            for j in range(0,len(words)-i-1):
                if words[j][1]>words[j+1][1]:
                    temp=words[j]
                    words[j] =words[j+1]
                    words[j+1]=temp
        print(words)

        listoflists = [['a',12],['d',123],['b',13],['q',5],['b',45]]
        for i in range(0, len(listoflists)):
            for j in range(0, len(listoflists) - i - 1):
                if (listoflists[j][1] > listoflists[j + 1][1]):
                    temp = listoflists[j]
                    listoflists[j] = listoflists[j + 1]
                    listoflists[j + 1] = temp

        print("List sorted based on second elem :",listoflists)

    """Python Program to Sort a List According to the Length of the Elements"""
    def sortbasedonlength(self):
        words = ["red","roker","bee","storyteller","wordings"]
        words.sort(key=len)
        print("List sorted based on length of words :",words)

    def unionList(self,lst):
        words= ['v','b','a','f','s','f','g','w']
        lst.extend(words)
        print ("Union of two lists :",lst)

    def bubblessort(self):
        lst = [122, 5, 11, 45, 1, 87, 4]
        for i in range(0, len(lst)):
            for j in range(0, len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    temp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = temp
        print(lst)

    def listOfTupleSquare(self):
        top = (2, 6, 1, 4)
        lst = []
        for i in top:
            new = list([i, i ** 2])
            lst.append(new)
        print(lst)

    def perfectsqsumoflist(self):
        # print(100**0.5)
        lst = [x for x in range(100, 399) if ((x ** 0.5) ** 2 == x) and sum(list(map(int, str(x)))) < 10]
        print(lst)



myList = [1,2,3,4,5,6,7,8,9,10]
obj = listsProg()
#obj.largeList(myList)
#obj.secondLargest(myList)
#obj.evenodd(myList)
#obj.sortmerge(myList)
#obj.sortbysecondelem()
#obj.bubblessort()
obj.listOfTupleSquare()
#obj.perfectsqsumoflist()
#obj.sortbasedonlength()
#obj.unionList(myList)

