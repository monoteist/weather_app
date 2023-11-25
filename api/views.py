from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from .serializers import CitySerializer
from weather.models import City
from weather.services import get_weather


class WeatherAPIView(views.APIView):
    def get(self, request):
        city_name = request.query_params.get('city')

        if not city_name:
            return Response({'error': 'Не указан город'}, status=status.HTTP_400_BAD_REQUEST)

        city = get_object_or_404(City, name__iexact=city_name)

        weather_data = get_weather(city.lat, city.lon)
        
        if not weather_data:
            return Response({'error': 'Не удалось получить данные о погоде'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        serializer = CitySerializer(city)
        city_data = serializer.data
        city_data['weather'] = weather_data

        return Response(city_data, status=status.HTTP_200_OK)
