class PyProg:
    def numRepresentator(self):
        """Find out the number is positive or negative """
        num = int(input("Enter the num > "))
        if num>0:
            print(num," Number is positive Number")
        else:
            print(num, " Number is Negative Number")

    def reverseNum(self):
        """Reverse the num """
        num = int(input("Enter the num to reverse > "))
        rev =0
        while(num>0):
            dig = num%10
            rev = rev*10+dig
            num =num//10
        print("Reverse Num = ",rev)

    def reverseString(self):
        """Reverse String"""
        str = input("Enter the num to reverse > ")
        lst = list(str)
        lst.reverse()
        print("Reversed String = ","".join(lst))

    def exchangeNum(self):
        """Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable"""
        a = int(input("Enter First num >"))
        b = int(input("Enter Second num >"))
        a = a + b
        b = a - b
        a = a - b
        print("A = ", a, "B = ", b)

    def complexEq(self):
        """Read a Number n and Compute n+nn+nnn"""
        num = int(input("Enter the num for complex eq > "))
        num1 = int(input("Enter the num for iterations > "))
        sum = 0
        for i in range(num1+1):
            temp = 0
            for j in range(0,i):
                temp = temp + pow(10,j) * num
            sum = sum + temp

        print(" Ans to complex eq = ",sum)

    def numCombo(self):
        num = input("Enter the num for numCombinations > ")
        lst = list(num)
        for i in range(len(lst)):
            for j in range(len(lst)):
                for k in range(len(lst)):
                    if ((i!=j) and (j!=k) and (k!=i)):
                        print(lst[i], lst[j], lst[k])



pyprog = PyProg()
print(" Here are the programs which can be attempted - ",
      "1. Check Whether a Number is Positive or Negative",
      "2. reverse the number",
      "3. reverse the string",
      "4. Exchange two numbers ")

test = int(input("Enter the num > "))

if test ==1:
    pyprog.numRepresentator()
elif test ==2:
    pyprog.reverseNum()
elif test ==3:
    pyprog.reverseString()
elif test == 4:
    pyprog.exchangeNum()
elif test == 5:
    pyprog.complexEq()
elif test == 6:
    pyprog.numCombo()
elif test == 6:
    pyprog.numCombo()
elif test == 6:
    pyprog.numCombo()
elif test == 6:
    pyprog.numCombo()
elif test == 6:
    pyprog.numCombo()
elif test == 6:
    pyprog.numCombo()