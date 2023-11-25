import os
from http import HTTPStatus

from dotenv import load_dotenv
import requests

load_dotenv()

YANDEX_WEATHER_API_KEY = os.getenv('YANDEX_WEATHER_API_KEY')
BASE_WEATHER_URL = os.getenv('BASE_WEATHER_URL')


def extract_weather_info(weather_data):
    '''
    Извлекает информацию о текущей погоде из данных, полученных от Yandex API.

    Parameters:
    - weather_data (dict): Данные о погоде от Yandex API.

    Returns:
    - dict: Словарь с информацией о текущей погоде, включая температуру, атмосферное давление и скорость ветра.
      Если какой-то ключ отсутствует, возвращает None.
    '''
    try:
        current_weather = weather_data['fact']
        temperature_celsius = current_weather['temp']
        atmospheric_pressure_mm = current_weather['pressure_mm']
        wind_speed_m_s = current_weather['wind_speed']

        return {
            'temperature_celsius': temperature_celsius,
            'atmospheric_pressure_mm': atmospheric_pressure_mm,
            'wind_speed_m_s': wind_speed_m_s,
        }
    except KeyError:
        return


def get_weather(lat, lon):
    '''
    Получает данные о погоде для указанных координат.

    :param lat: Широта (latitude)
    :param lon: Долгота (longitude)

    :return: JSON-данные о погоде для указанных координат.
    '''

    params = {
        'lat': lat,
        'lon': lon,
    }
    headers = {
        'X-Yandex-API-Key': YANDEX_WEATHER_API_KEY
    }

    response = requests.get(BASE_WEATHER_URL, params=params, headers=headers)
    
    if response.status_code == HTTPStatus.OK:
        weather_data = response.json()
        return extract_weather_info(weather_data)
