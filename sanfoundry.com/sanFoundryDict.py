class dictProg():

    def addinfo(self):
        """Python Program to Add a Key-Value Pair to the Dictionary"""
        newdict ={1:"aa",2:"bb",3:"cc",4:"dd",5:"ee"}
        newdict[6]="ff"
        newdict.update({7:"gg"})
        print(newdict)


    def dict_combo(self):
        newdict = {1: "aa", 2: "bb", 3: "cc", 4: "dd", 5: "ee"}
        newdict1 = {"a": 11, "b": "22", "c": 33, "d": 44, "e": 55}

        newdict.update(newdict1)
        print(newdict)

    def keyexist(self):
        k = 7
        newdict = {1: "aa", 2: "bb", 3: "cc", 4: "dd", 5: "ee"}
        if k in newdict.keys():
            print("Key Exists")
        else:
            print("Key not found")

    def generateDict(self):
        d = {}
        n=10
        for i in range(1,n+1):
            d.update({i:i*i})
        print(d)

    def dictSum(self):
        newdict1 = {"a": 10, "b": "20", "c": 30, "d": 40, "e": 50}
        print(sum(map(int,newdict1.values())))

    def dictmulti(self):
        newdict1 = {"a": 10, "b": "20", "c": 30, "d": 40, "e": 50}
        multi = 1
        #print(sum(map(int,newdict1.values())))
        for value in newdict1.values():
            multi = int(value) * multi

        print(multi)

obj = dictProg()
#obj.addinfo()
#obj.dict_combo()
#obj.keyexist()
#obj.generateDict()
#obj.dictSum()
obj.dictmulti()