from _sitebuiltins import _Printer

from io import open


class filehandling:

    filePath = "G:\Learning_Curves\headFirstPython\headFirstPython\story.txt"

    def read_content(self):
        with open(filehandling.filePath,'r') as f:
            for line in f:
                print(line,end='')

    def wordcount(self):
        count = 0
        with open(filehandling.filePath,'r') as f:
            for line in f:
                wrd = line.split(" ")
                count += len(wrd)
            print ("count of words in file >>",count)


    def linecount(self):
        count = 0
        with open(filehandling.filePath,'r') as f:
            for line in f:
                count += 1
            print ("count of line in file >>",count)

    def fileappend(self):
        with open("new.txt",'a') as f:
            str = input("ENter a line : >")
            f.write("\n")
            f.write(str)
        with open("new.txt",'r') as a:
            for line in a:
                print(line)

    def countofword(self):
        k=0
        word = "the"
        with open(filehandling.filePath,'r')as f:
            for line in f:
                words = line.split()
                for i in words:
                    if (i == word):
                        k = k + 1
            print("Occurance of the in file >",k)

    def copycontent(self):
        with open("new.txt",'r') as f:
            with open("another.txt",'w') as f1:
                for line in f:
                    f1.write(line)

        with open("another.txt", 'r') as f:
            for line in f:
                print(line)

    def lettercount(self):
        l="A"
        k=0
        with open("new.txt",'r') as f:
            for line in f:
                word = line.split()
                for i in word:
                    for letter in i:
                        if(letter == l):
                            k+=1
        print("Occurance of letter",k)

    def num_in_file(self):
        with open("new.txt", 'r') as f:
            for line in f:
                word = line.split()
                for i in word:
                    for letter in i:
                        if (letter.isdigit()):
                            print(letter)


    def reverseread(self):
        for line in reversed(list(open("ReadMe.txt"))):
            print(line.rstrip())


obj = filehandling()
#obj.read_content()
#obj.wordcount()
#obj.linecount()
#obj.fileappend()
#obj.countofword()
#obj.copycontent()
#obj.lettercount()
#obj.num_in_file()
obj.reverseread()