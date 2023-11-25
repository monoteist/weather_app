from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from weather.models import City


class WeatherAPITestCase(TestCase):
    def setUp(self):
        self.city = City.objects.create(
            name='Moscow', lat=55.755787, lon=37.617634)
        self.client = APIClient()

    @patch('api.views.get_weather')
    def test_get_weather_api_view_with_external_api(self, mock_get_weather):
        mock_get_weather.return_value = {
            'temperature_celsius': 25,
            'atmospheric_pressure_mm': 760,
            'wind_speed_m_s': 3,
        }

        url = reverse('api:weather')

        response = self.client.get(url, {'city': 'Moscow'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('name', response.data)
        self.assertIn('weather', response.data)

        expected_weather_data = {
            'temperature_celsius': 25,
            'atmospheric_pressure_mm': 760,
            'wind_speed_m_s': 3,
        }
        self.assertEqual(response.data['weather'], expected_weather_data)
