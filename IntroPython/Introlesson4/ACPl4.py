#Create a program to calculate the square root.
import math 
num = int(input("Enter a number to find the square root: "))
sqrt = math.sqrt(num)
print("The square root of", num, "is", sqrt)

#Create a program to calculate the square root using exponentiation operator.
num = int(input("Enter a number to find the square root using exponentiation operator: "))
sqrt = num ** 0.5
print("The square root of", num, "is", sqrt)
#Create a program to calculate the square root using pow() function.
num = int(input("Enter a number to find the square root using pow() function: "))           
sqrt = pow(num, 0.5)
print("The square root of", num, "is", sqrt)
#Create a program to calculate the square root using fractional exponent.
num = int(input("Enter a number to find the square root using fractional exponent: "))
sqrt = num ** (1/2)
print("The square root of", num, "is", sqrt)

