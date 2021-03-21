class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def perimeter(self):
        print("Perimeter: ",self.l+self.b)
    def area(self):
        print("Area: ",self.l*self.b)
ob=rect(5,6)
ob.perimeter()
ob.area()
