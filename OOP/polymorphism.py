import math

class shape:
    def area(self):
        print('Undefined')

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print('Area of circle is',math.pi*(self.radius**2))

class square(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        print('Area of square is',self.side**2)

s=[circle(5) , square(2)]
for a in s:
    a.area()
