#Write a program to calculate the n number power of a given number? using loops
# input base number
base = float(input("Enter the base number: "))
# input exponent number
exponent = int(input("Enter the exponent number: "))
# initialize result
result = 1
# loop to calculate power
for i in range(exponent):
    result = result * base
# print the result
print(f"{base} raised to the power of {exponent} is: {result}")
    