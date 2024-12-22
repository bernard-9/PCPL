from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.color import FigureColor

class Rectangle(GeometricFigure):

    shape_name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height
    
    def __repr__(self):
        return "ширина: {}, высота: {}, цвет: {}, площадь: {:.2f}".format(
            self.width, self.height, self.color.color, self.area()
        )

    @classmethod
    def get_shape_name(cls):
        return cls.shape_name