""" 
Принцип открытости закрытости

Подразуемевает:
- Что класс открыт для расширения но закрыт для модификации

"""
from enum import Enum

# Цвет продукта
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Размер продукта
class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# Продукт
class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# Фильтрация продукции
# !! В зависимости от колличества фильтров, класс можно расширять бесконечно долго
class ProductFilter:
    # По цвету
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p
    # По размеру
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p
    # По размеру и цвету 
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p



"""  Реализация согласно OSP """

# Класс проверяет удовлетворяет ли элкмент определенному критерию 
class Specification:

    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

bf = BetterFilter()

print('Green products (new):')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f' - {p.name} is green')

print('Large products:')
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f' - {p.name} is large')

print('Large blue items:')
large_blue = large & ColorSpecification(Color.BLUE)
for p in bf.filter(products, large_blue):
    print(f' - {p.name} is large and blue')