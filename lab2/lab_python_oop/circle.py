from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.color import FigureColor
import math

class Circle(GeometricFigure):

    shape_name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __repr__(self):
        return "радиус: {}, цвет: {}, площадь: {:.2f}".format(
            self.radius, self.color.color, self.area()
        )
    
    @classmethod
    def get_shape_name(cls):
        return cls.shape_name