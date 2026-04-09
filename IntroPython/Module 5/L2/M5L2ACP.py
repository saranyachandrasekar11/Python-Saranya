import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
my_circle = Circle(5)
print(f"Area: {my_circle.get_area():.2f}")
print(f"Perimeter: {my_circle.get_perimeter():.2f}")
