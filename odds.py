from datetime import datetime

odd=[1,3,5,7,9,11,3,15,17,19,21,23,25,27,
     29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute
today = datetime.today().weekday()
print (today)
for super in range (10):
    if today == 5:
        print ("Yayyy!!! Weekend !!!")
    elif today !=5:
        if right_this_minute in odd:
            print ("This is very odd time to work")
        else:
            print ("This is the time to get even.")
    else:
        print (" I will work tomorrow ")
