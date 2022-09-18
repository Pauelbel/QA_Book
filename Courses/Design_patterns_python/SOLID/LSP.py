""" 
Принцип подстановки лисков

Подразуемевает:
- Если есть API принимающий базовый класс, то должнать быть возможность
передать туда любой произвольный класс
"""


class Rectangle:
    # Конструктор могет с шириной и высотой
    # __height и _width условно трогать ненужно
    def __init__(self, width, height):
        self._height = height
        self._width = width

    # Свойство для вычисления площади
    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'
    
    # Свойство для ширины
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    # Свойство для высоты
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

""" Нарушить принцип можно так """
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value

# Метод для использования класса Rectangle
def use_it(rc):
    w = rc.width
    rc.height = 10  # Побочный ефект который помогает нарушить принцип
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)
use_it(rc)

# sq = Square(5)
# use_it(sq)
