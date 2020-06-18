from oop.MultipleInheritance.square import Square
from oop.MultipleInheritance.triangle import Triangle

s1 = Square()
s1.set_value(8,15)
s1.set_color("Blue")
print( s1.area(),s1.get_color())

s2 = Triangle()
s2.set_value(8,15)
s2.set_color("Green")
print(s2.area(),s2.get_color())

