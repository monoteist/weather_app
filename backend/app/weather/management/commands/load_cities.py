import json

from django.core.management.base import BaseCommand
from weather.models import City

class Command(BaseCommand):
    help = 'Load cities data from JSON file into the database'

    def handle(self, *args, **options):
        file_path = "app/weather/cities_with_coordinates.json"

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for city_name, coordinates in data.items():
            lat = coordinates['lat']
            lon = coordinates['lon']
            
            City.objects.update_or_create(name=city_name, defaults={'lat': lat, 'lon': lon})

        self.stdout.write(self.style.SUCCESS('Cities data loaded successfully.'))
