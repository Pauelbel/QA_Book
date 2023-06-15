# Пример Dockerfile
# Создание образа на основе Python, установка дополнительных пакетов и копирование приложения внутрь контейнера:

# Указываем базовый образ, на котором основан наш новый образ
FROM python:3.8-slim-buster

# Добавляем метаданные
ARG name='pvb.tester'
ARG email='pvb.tester@gmail.com'
LABEL 'maintainer'=${name}

# Запускаем все команды от рута
USER root

# Устанавливаем дополнительные пакеты, необходимые для нашего приложения
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-setuptools \
    nginx \
    curl \
    libpq-dev

# Устанавливаем зависимости Python из requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Копируем наше приложение внутрь контейнера
COPY . /app

# Определяем рабочую директорию контейнера
WORKDIR /app

# Настраиваем nginx
# COPY ./config/nginx.conf /etc/nginx/nginx.conf
# RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    # && ln -sf /dev/stderr /var/log/nginx/error.log

# Определяем команду, которая будет выполняться при старте контейнера
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]


# Чтобы создать образ из этого Dockerfile, необходимо выполнить команду docker build в терминале, находясь в той же директории, где находится файл Dockerfile.