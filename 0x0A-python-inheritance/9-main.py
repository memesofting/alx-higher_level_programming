#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

r = Rectangle(3, 5)

print(r)
print(r.area())
print(issubclass(Rectangle, BaseGeometry))
