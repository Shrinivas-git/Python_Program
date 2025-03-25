from abc import ABC
class shape(ABC):
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
class rectangle(shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
rect=rectangle(5,10)
print(f"Area{rect.area()}")
print(f"Perimeter{rect.perimeter()}")
    