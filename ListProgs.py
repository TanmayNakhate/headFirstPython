from builtins import print
from turtledemo import sorting_animate


class listProg:
    def largestNuminList(self,lst):
        """ Returns max from provided list"""
        return max(lst)

    def calculateLargestnum(self,lst):
        temp = 0
        for i in lst:
            a = i;
            if a>temp:
                temp=a
        return temp

    def sortMax(self,lst):
        lst.sort()
        return lst[len(lst)-1]



