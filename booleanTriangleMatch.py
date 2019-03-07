def trianglefinder(x,y,z):
    if int(x)==int(y) and int(y)==int(z):
        print("Equilateral")
    elif int(x)!=int(y) and int(y)!=int(z) and int(x)!=int(z):
        print("Scalene")
    else:
        print("Isosceles")


trianglefinder(20,20,30)
