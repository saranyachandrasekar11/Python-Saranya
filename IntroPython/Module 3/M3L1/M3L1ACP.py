#Write a program to create a python function to calculate the circumference of a circle?

import math
def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference
# Taking input from the user
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print("The circumference of the circle with radius", radius, "is:", circumference)

    