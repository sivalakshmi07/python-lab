import math
class Shape:
    def area(self):
        print("Calculating area... ")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Rectangle area:", self.length * self.width)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("Circle area:", math.pi * self.radius ** 2)
print("Rectangle:")
rect = Rectangle(5, 3)
rect.area()            
super(Rectangle, rect).area()  
print("\nCircle:")
circle = Circle(4)
circle.area()             
super(Circle, circle).area()   
