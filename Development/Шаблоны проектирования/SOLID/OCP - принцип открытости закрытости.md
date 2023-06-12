Согласно принципу OCP, программное обеспечение должно быть открыто для расширения и закрыто для модификации.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print('Processing payment using credit card for amount:', amount)

class MobileWalletPayment(Payment):
    def pay(self, amount):
        print('Processing payment using mobile wallet for amount:', amount)

class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        payment_method.pay(amount)

cc_payment = CreditCardPayment()
mw_payment = MobileWalletPayment()
processor = PaymentProcessor()

processor.process_payment(cc_payment, 100)
processor.process_payment(mw_payment, 50)
```

У нас есть абстрактный класс `Payment`, который имеет метод `pay`. Два класса, `CreditCardPayment` и `MobileWalletPayment`, реализуют абстрактный метод собственным способом.

`PaymentProcessor` класс использует разные методы оплаты, передаваемые ему как параметр, и вызывает метод `pay` для обработки платежа.

Это делает класс `PaymentProcessor` открытым для расширения, так как мы можем добавлять новые методы оплаты, используя наш шаблон (`Payment`), при этом не изменяя существующий код. А класс `PaymentProcessor` закрыт для модификации, так как нет необходимости изменять его код при добавлении новых методов оплаты