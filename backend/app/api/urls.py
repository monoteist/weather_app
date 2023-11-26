from django.urls import path 

from .views import WeatherAPIView

app_name = 'api' 

urlpatterns = [ 
    path('weather', WeatherAPIView.as_view(), name='weather'), 
]