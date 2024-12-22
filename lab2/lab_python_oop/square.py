from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import FigureColor

class Square(Rectangle):

    shape_name = "Квадрат"

    def __init__(self, side, color):
        self.side = side
        self.color = FigureColor(color)

    def area(self):
        return self.side ** 2
    
    def __repr__(self):
        return "сторона: {}, цвет: {}, площадь: {:.2f}".format(
            self.side, self.color.color, self.area()
        )

    @classmethod
    def get_shape_name(cls):
        return cls.shape_name