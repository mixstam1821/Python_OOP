import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius

# Example usage:
circle1 = Circle(5)
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())
