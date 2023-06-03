Принцип единственной ответственности (Single Responsibility Principle, SRP) гласит, 
что каждый класс или функция должны иметь только одну ответственность, то есть выполнять только один набор связанных задач.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # код для сохранения пользователя в базу данных
        
    def send_email(self, message):
        # код для отправки электронной почты пользователю
```

В этом примере класс `User` имеет две обязанности - сохранение пользователя в базу данных и отправку ему электронной почты. Чтобы улучшить этот класс и следовать принципу SRP, мы можем разделить его на два класса:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
class UserRepository:
    def save(self, user):
        # код для сохранения пользователя в базу данных
        
class EmailService:
    def send_email(self, user, message):
        # код для отправки электронной почты пользователю
```