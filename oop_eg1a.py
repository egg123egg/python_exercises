###python program to find the area of a triangle using Classes.
class triangle():
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return (self.base*self.height)/2
a=int(input('Enter base of triangle: '))
b=int(input('Enter height of triangle: '))
obj= triangle(a,b)
print("Area of triangle: ",obj.area())
print()