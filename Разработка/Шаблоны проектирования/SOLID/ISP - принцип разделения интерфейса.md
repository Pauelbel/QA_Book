Согласно принципу ISP, клиенты не должны зависеть от интерфейсов, которые они не используют. 
Вместо этого интерфейсы должны быть разделены на маленькие и специфичные, 
чтобы клиенты могли реализовывать только те интерфейсы, которые им действительно нужны.

```python
from abc import ABC, abstractmethod

# Интерфейс для отправки сообщения по email
class EmailSenderInterface(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> None:
        pass

# Интерфейс для отправки сообщения через SMS (телефон)
class SMSSenderInterface(ABC):
    @abstractmethod
    def send_sms(self, to: str, message: str) -> None:
        pass

# Класс обработки оповещений
class NotificationService:
    def __init__(self, email: EmailSenderInterface, sms: SMSSenderInterface):
        self.email = email
        self.sms = sms

    def send_notification(self, user_id: int, message: str) -> None:
        email = self.get_user_email_by_id(user_id)
        phone = self.get_user_phone_by_id(user_id)
        self.email.send_email(email, "Notification", message)
        self.sms.send_sms(phone, message)

    def get_user_email_by_id(self, user_id: int) -> str:
        # Пусть тут будет заглушка
        return "example@mail.com"

    def get_user_phone_by_id(self, user_id: int) -> str:
        # Пусть тут будет заглушка
        return "79991234567"

# Класс для отправки сообщений по email
class EmailSender(EmailSenderInterface):
    def send_email(self, to: str, subject: str, body: str) -> None:
        print(f"Sending email to {to} with subject \"{subject}\" and body \"{body}\"")

# Класс для отправки сообщений по sms
class SMSSender(SMSSenderInterface):
    def send_sms(self, to: str, message: str) -> None:
        print(f"Sending sms to {to} with message: {message}")
```

В этом примере мы разделили интерфейсы `EmailSenderInterface` и `SMSSenderInterface`, чтобы клиенты могли реализовывать только нужные им методы.

Класс `NotificationService` использует интерфейсы `EmailSenderInterface` и `SMSSenderInterface`, чтобы отправлять оповещения пользователям по электронной почте и через SMS. Классы `EmailSender` и `SMSSender` реализуют соответствующие интерфейсы и используют конкретные способы отправки сообщений.

Таким образом, мы можем использовать любой класс, реализующий соответствующие интерфейсы, чтобы отправить сообщения пользователям. Клиенты не зависят от конкретных классов и методов,