with open("affinity.txt",'r')as f:
    words = []
    line = f.read()
    line = line.splitlines()
    for l in line:
        words.extend(l.split(" "))
    for i in range(0,len(words)-1,4):
        #print(words[i], "<==>",words[i+1]," <=>", words[i+3])
        #try:
            if words[i+1]==words[i+3]:
                print("Anti-Affinity Failed for ",words[i])
            else:
                print("Anti-Affinity passed for ",words[i])
        #except IndexError:
            #print("Anti-Affinity Failed for ", words[i])
            #print("Please check anti affinity for failed pods manually")
            #continue


