from builtins import print


class setprogs:

    def num_vowels(self):
        """Python Program to Count the Number of Vowels Present in a String using Sets"""
        str = "SuperWoMan"
        count=0
        vowel=set(list("aeiou"))
        for i in str:
            for j in vowel:
                if(i==j):
                    count+=1
        print(count)

    def common_letters(self):
        """Python Program to Check Common Letters in Two Input Strings"""
        str = "SuperWoMan"
        str1 = "IronMans"
        print(list(set(str)&set(str1)))
        print(set(str).intersection(set(str1)))

    def lettrs_not_in_2string(self):
        """Python Program that Displays which Letters are in the First String but not in the Second"""
        str = "HulkHogan"
        str1 = "Hulk"

        print(list(set(str)-set(str1)))
        newSet=set(str).difference(set(str1))
        print(newSet)

    def common_lettrs_in_2string(self):
        """Python Program that Displays which Letters are Present in Both the Strings"""
        str = "HulkHogan"
        str1 = "Hulk"

        print(list(set(str)|set(str1)))
        newSet=set(str).union(set(str1))
        print(newSet)

    def lettrs_but_notin_2string(self):
        """Python Program that Displays which Letters are in the Two Strings but not in Both"""
        str = "HulkHogan"
        str1 = "Hulk"

        print(list(set(str)^set(str1)))
        newSet=set(str).symmetric_difference(set(str1))
        print(newSet)


obj=setprogs()
#obj.num_vowels()
obj.common_letters()
obj.lettrs_not_in_2string()
obj.common_lettrs_in_2string()
obj.lettrs_but_notin_2string()