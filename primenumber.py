n=53
if n%2 is 0:
    print("n is not prime")
    for i in range(3,n):
        if n%i is 0:
            print("n is not prime")
            break
else:
    print("n is prime")
