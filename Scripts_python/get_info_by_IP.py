""" 
Получить информацию об устройстве по IP адресу
Подсмотрел тут - https://www.youtube.com/watch?v=IZOq_sOtLz0
"""

import requests

IP = '178.155.16.159'

def get_info(ip):
    try:
        resp = requests.get(f'http://ip-api.com/json/{IP}').json()
        
        r_data = {
            'IP': resp.get('query'),
            'Индекс': resp.get('zip') or None,
            'Регион': resp.get('regionName') or None,
            'Город': resp.get('city') or None,
            'Широта': resp.get('lat') or None,
            'Долгота': resp.get('lon') or None,
        }
        for k, v in r_data.items():
            print(f'{k}:{v}')

    except:
        if requests.exceptions.ConnectionError == True:
            print("Проблема с подключением")
        else:
            print("Проверь IP адрес")

if __name__ == '__main__':
    info = get_info(IP)