""" 
Принцип разделения интерфейса

Подразуемевает:
- Что не стоит добавлять слишком много методов в интерфейс
"""
from abc import abstractmethod

# Интерфейс машины
class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ОК мы можем переопределить методы и что-то с ними делать дальше
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

""" 
Принцип нарушается т.к принтер не имеет факса и не может печатать
но при этом эти функции будут доступны при определении класса
"""
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')

""" 
Правильно будет деталезировать каждый класс
для печати класс Printer для сканера Scanner и т.д.
"""
class Printer:
    @abstractmethod
    def print(self, document): pass


class Scanner:
    @abstractmethod
    def scan(self, document): pass


# Если нужен принтер
class MyPrinter(Printer):
    def print(self, document):
        print(document)

# Если нужен принтер и сканнер
class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass 

# Если нужно МФУ
class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!
