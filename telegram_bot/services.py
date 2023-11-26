import os
from http import HTTPStatus

from dotenv import load_dotenv
import requests

load_dotenv()

YANDEX_WEATHER_API_KEY = os.getenv('YANDEX_WEATHER_API_KEY')
BASE_WEATHER_URL = os.getenv('BASE_WEATHER_URL')


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
        today_forecast = weather_data.get('forecasts', [{}])[
            0].get('hours', [])
        result_dict = {}
        for hour_data in today_forecast:
            hour = hour_data.get('hour')
            temperature = hour_data.get('temp')
            result_dict[hour] = temperature

        return result_dict
