###python program to find the area of a Rectangle using Classes.
class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input('Enter lenght of rectangle: '))
b=int(input('Enter breadth of rectangle: '))
obj= rectangle(a,b)
print("Area of rectangle: ",obj.area())
print()
        