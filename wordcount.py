import sys
import re
import csv

file = sys.argv[1]
dict={}
csv_columns = {'Word':'Count'}
with open(file,'r') as f:
    freader = f.readlines()
    for line in freader:
        line = re.sub(r'[^\w\s]','',s)
        word = line.split(" ")
        for i in word:
            if i in dict.keys():
                dict[i] +=1
            else:
                dict.update({i:1})
    print("Word count >>",dict.keys(),dict.values())

    with open('newFile.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        #writer.writeheader()
        for key, val in dict.items():
            writer.writerow([key, val])
    print("Word count >>",dict)