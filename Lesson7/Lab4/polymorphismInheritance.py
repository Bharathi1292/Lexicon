class Shape:
    def area(self):
        raise NotImplementedError("This method must be implemented by subclasses")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2
def print_area(shape_obj):
    print("Area is :", shape_obj.area())
r = Rectangle(10, 5)
c = Circle(7)
print_area(r) 
print_area(c)  

