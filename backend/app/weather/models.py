from django.db import models

class City(models.Model):
    name = models.CharField('Название города', max_length=50)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
