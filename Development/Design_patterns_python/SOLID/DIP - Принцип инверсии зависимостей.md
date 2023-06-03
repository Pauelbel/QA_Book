Согласно принципу DIP, модули верхнего уровня не должны зависеть от модулей нижнего уровня. 
Оба типа модулей должны зависеть от абстракций. Абстракции не должны зависеть от деталей реализации. 
Детали реализации должны зависеть от абстракций.

```python
from abc import ABC, abstractmethod

# Интерфейс для отправки сообщений
class MessageSenderInterface(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> None:
        pass

# Модуль для отправки сообщений через email
class EmailSender(MessageSenderInterface):
    def send(self, to: str, message: str) -> None:
        print(f"Sending email to {to} with message: {message}")

# Модуль для отправки сообщений через SMS
class SMSSender(MessageSenderInterface):
    def send(self, to: str, message: str) -> None:
        print(f"Sending sms to {to} with message: {message}")

# Модуль для отправки уведомлений
class NotificationService:
    def __init__(self, message_sender: MessageSenderInterface):
        self.message_sender = message_sender

    def send_notification(self, user_id: int, message: str) -> None:
        email = self.get_user_email_by_id(user_id)
        phone = self.get_user_phone_by_id(user_id)
        self.message_sender.send(email, message)
        self.message_sender.send(phone, message)

    def get_user_email_by_id(self, user_id: int) -> str:
        # Пусть тут будет заглушка
        return "example@mail.com"

    def get_user_phone_by_id(self, user_id: int) -> str:
        # Пусть тут будет заглушка
        return "79991234567"
```

В этом примере модули `EmailSender` и `SMSSender` реализуют интерфейс `MessageSenderInterface`, который определяет метод `send` для отправки сообщения.

Модуль `NotificationService` зависит только от абстракции `MessageSenderInterface` и использует метод `send` для отправки сообщений. Модуль `NotificationService` может использовать любой класс, реализующий интерфейс `MessageSenderInterface`, для отправки сообщений без изменения кода.

Таким образом, мы инвертировали зависимость между модулями `NotificationService` и `MessageSenderInterface`, делая код более гибким и легко расширяемым. Мы можем добавлять новые модули для отправки сообщений, реализующие интерфейс `MessageSenderInterface`, без изменения кода `NotificationService`.