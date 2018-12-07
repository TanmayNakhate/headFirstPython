"""Python Program to Read a Mumber n and Compute n+nn+nnn"""

n = int(input("Enter the number > "))

# Converting the number to string
str_n = str(n)

# Initializing result as number and string
sums = n
sum_str = str(n)

# Adding remaining terms
for i in range(1, 3):
    # Concatenating the string making n, nn, nnn...
    sum_str = sum_str + str_n

    # Before adding converting back to integer
    sums = sums + int(sum_str)

print("Sum ",sums)
