import csv
from datetime import datetime


#print(dir(csv))
path = "T:\headFirstPython\GOOG.csv"
file = open(path,newline='')
reader = csv.reader(file)

header = next(reader)
print(header)
#['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
#data = [row for row in reader]
#print(data[0])
data=[]
#['2019-01-07', '1071.500000', '1074.000000', '1054.760010', '1068.390015', '1068.390015', '1981900']
for row in reader:
    date = datetime.strptime(row[0],'%Y-%m-%d')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    adj_close = float(row[5])
    volume = int(row[6])
    data.append([date,open_price,high,low,close,adj_close,volume])


print(data[0])
