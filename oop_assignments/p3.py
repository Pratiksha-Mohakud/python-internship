import math

# creating a class

class circle():
    def __init__(self,x,y,radius):  # initializing the attributes
        self.x=x
        self.y=y
        self.radius=radius
# defining methods
    def get_area(self):
        area=math.pi*self.radius**2
        return area
    def get_perimeter(self):
        perimeter=2*math.pi*self.radius
        return perimeter
    def get_circumference(self):
        return self.get_perimeter()
    
# taking inputs
x=int(input("Enter the x coordinate of centre:"))
y=int(input("Enter the y coordinate of centre:"))
radius=float(input("Enter the radius of the circle: "))
obj=circle(x,y,radius) # passing values to class

# calling the methods one by one
print(obj.get_area())  
print(f"perimeter is{obj.get_perimeter()}.2f")
print(obj.get_circumference())

    
