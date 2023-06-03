Согласно принципу LSP, объекты в программе должны быть заменяемы друг за друга, 
если они принадлежат к одному и тому же классу, не нарушая работу программ

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size * self.size

def print_area(shape):
    print(f"Area of the shape is: {shape.area()}")

rect = Rectangle(5, 10)
 sqr = Square(7)

print_area(rect)
print_area(sqr)
```

В этом примере классы `Rectangle` и `Square` наследуют класс `Shape`, определяющий метод `area`. Объект `Rectangle` представляет собой прямоугольник со свойствами `width` и `height`, а объект `Square` - квадрат с размером `size`.

Функция `print_area` принимает объект класса `Shape` и вызывает метод `area`. Эта функция может использовать любой объект класса, унаследованного от `Shape`, чтобы вычислить площадь фигуры.

Таким образом, мы можем заменить объект класса `Rectangle` объектом класса `Square` без каких-либо изменений в программе, так как оба класса являются наследниками класса `Shape` и имеют метод `area`. Мы не нарушаем работу программы, следуя принципу LSP.