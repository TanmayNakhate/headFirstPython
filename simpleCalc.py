class calculation:

    @classmethod
    def add(cls, x, y):
        """Addition of two numbers"""
        return float(x) + float(y)

    @classmethod
    def sub(cls, x, y):
        """Subtraction of two numbers"""
        return float(x) - float(y)

    @classmethod
    def multi(cls, x, y):
        """Multiplication of two numbers"""
        return float(x) * float(y)

    @classmethod
    def div(cls, x, y):
        """Division of two numbers"""
        return float(x) / float(y)

    @classmethod
    def numChecker(cls):
        """num validator """
        x = input("Enter first number >")
        while x.isalnum() or x.isalpha():
            if x.isdigit():
                break
            x = input("Enter first number >")
        y = input("Enter second number >")
        while y.isalnum() or y.isalpha():
            if y.isdigit():
                break
            y = input("Enter second number >")
        return x,y


    @classmethod
    def selection(self):

        print("\n\nWelcome to simple calculator :\n",
              "Select opration to carry >>\n",
              "1. Addition of two numbers\n",
              "2. Subtraction of two numbers\n",
              "3. Multiplication of two numbers\n",
              "4. Division of two numbers\n",
              "5. Exit\n\n")
        num = int(input(">>"))
        if num!=5:
            calculation.repeat(num)

    @classmethod
    def repeat(cls,num):
        while (num):
            if num == 1:
                print("You have selected addition.")
                x,y = calculation.numChecker()
                ans = calculation.add(x, y)
                print("Addition of %s,%s is %d " % (x, y, ans))
                break
            if num == 2:
                print("You have selected Subtraction.")
                x,y = calculation.numChecker()
                ans = calculation.sub(x, y)
                print("Subtraction of %s,%s is %d " % (x, y, ans))
                break
            if num == 3:
                print("You have selected Multiplication.")
                x,y = calculation.numChecker()
                ans = calculation.multi(x, y)
                print("Multiplication of %s,%s is %d " % (x, y, ans))
                break
            if num == 4:
                print("You have selected Division.")
                x = input("Enter first number >")
                while x.isalnum() or x.isalpha():
                    if x.isdigit():
                        break
                    x = input("Enter first number >")
                y = input("Enter second number >")
                while y.isalnum() or y.isalpha():
                    if y.isdigit():
                        break
                    y = input("Enter second number >")
                ans = calculation.div(x, y)
                print("Division of %s,%s is %d " % (x, y, ans))
                break
        calculation.selection()


#obj = calculation()
calculation.selection()
