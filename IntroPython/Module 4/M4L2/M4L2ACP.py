#Write a Python program to calculate the product, multiplying all the numbers of the given tuple.no function
tuple1 = (2, 3, 4, 5)
product = 1

for i in range(0, len(tuple1)):
    product *= tuple1[i]
print("The product of the numbers in the tuple is:", product)

    
    