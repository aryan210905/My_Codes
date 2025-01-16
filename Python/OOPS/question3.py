import math
class Circle:
    def __init__(self,r):
        self.r = r
    
    @property
    def area(self):
        return 3.14 * self.r * self.r
    
    @property
    def circumference(self):
        return 2 * 3.14 * self.r
    
c1 = Circle(21)

print(c1.area)
print(c1.circumference)
    
    