# shape_area_system.py

import math

class Shape:
    def area(self_kdm):
        """Base method that will be overridden by child classes"""
        pass

class Rectangle(Shape):
    def __init__(self_kdm, length, width):
        self_kdm.length_kdm = length
        self_kdm.width_kdm = width
    
    def area(self_kdm):
        return self_kdm.length_kdm * self_kdm.width_kdm

class Circle(Shape):
    def __init__(self_kdm, radius):
        self_kdm.radius_kdm = radius
    
    def area(self_kdm):
        return math.pi * self_kdm.radius_kdm ** 2

class Triangle(Shape):
    def __init__(self_kdm, base, height):
        self_kdm.base_kdm = base
        self_kdm.height_kdm = height
    
    def area(self_kdm):
        return 0.5 * self_kdm.base_kdm * self_kdm.height_kdm

# Create instances of each shape
rectangle = Rectangle(10, 5)
circle = Circle(5)
triangle = Triangle(8, 6)

# Display the areas
print(f"Rectangle Area: {rectangle.area()}")
print(f"Circle Area: {circle.area()}")
print(f"Triangle Area: {triangle.area()}")

# Montes, Karen