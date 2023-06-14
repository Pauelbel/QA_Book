FROM python:alpine

# Рабочая директория где лежит app.py
WORKDIR /app

# Доустанавливаем зависимости для запуска app.py
RUN pip install pymongo

# Копируем все из текущей директории
COPY . .

# при запуске контейнера запустить питон и передать ему файл программы
CMD [ "python", "app.py" ]