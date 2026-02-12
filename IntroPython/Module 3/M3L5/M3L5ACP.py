#Trigonometric value
#Write a program to calculate the values of sin, cos, and tan using the math module.
import math #importing math module
angle = float(input("Enter an angle in degrees: ")) #take input from user
#using radians function to convert degree to radians
radians = math.radians(angle)
#using sin, cos and tan function to calculate the values
sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)
print(f"The sine of {angle} degrees is: {sin_value}")
print(f"The cosine of {angle} degrees is: {cos_value}")
print(f"The tangent of {angle} degrees is: {tan_value}")

    