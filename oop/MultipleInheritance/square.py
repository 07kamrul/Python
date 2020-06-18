from oop.MultipleInheritance.polygon import Polygon
from oop.MultipleInheritance.Shape import Shape

class Square(Polygon,Shape):
    def area(self):
        return self.get_width() * self.get_height()
