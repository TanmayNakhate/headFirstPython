vowels = ['a','e','i','o','u']
# word = "Tufani Ghode"
word = input("Provide Word to find vowels : ")
runtimeList = []
consonentList = []
for char in word:
    if char in vowels:
        print ("Here's a vowel character in word",char)
        runtimeList.append(char)
    elif char not in vowels:
        consonentList.append(char)
len(runtimeList)
print (runtimeList)
print (consonentList)
