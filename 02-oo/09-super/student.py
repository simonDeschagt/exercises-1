from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length
    
    @property
    def width(self):
        return self.__width
    
    @property
    def area(self):
        return self.length * self.width
    
    @property
    def perimeter(self):
        return (self.length + self.width) * 2
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    @property
    def side(self):
        return self.length
    
class Ellipse(Shape):
    def __init__(self, major_radius, minor_radius):
        self.__big_radius = major_radius
        self.__small_radius = minor_radius

    @property
    def major_radius(self):
        return self.__big_radius
    
    @property
    def minor_radius(self):
        return self.__small_radius

    @property
    def perimeter(self):
        raise NotImplementedError
    
    @property
    def area(self):
        return pi * self.__big_radius * self.__small_radius
    
class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)
        

    @property
    def area(self):
        return pi * self.radius **2

    @property
    def perimeter(self):
        return 2*pi*self.radius 
    
    @property
    def radius(self):
        return self.major_radius