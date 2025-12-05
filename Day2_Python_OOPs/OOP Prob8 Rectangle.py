class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        peri=2*(self.length+self.breadth)
        return f"The perimeter of rectangle is {peri}"
    def area(self):
        ar=self.length* self.breadth
        return f"The area of the rectangle is {ar}"

r1=Rectangle(20,25)
print(r1.perimeter())
print(r1.area())
