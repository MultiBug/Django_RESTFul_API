from django.db import models


class Car(models.Model):
    vin = models.CharField(verbose_name='VIN', db_index=True, max_length=64)
    color = models.CharField(verbose_name='Цвет', max_length=64)
    brand = models.CharField(verbose_name='Брэнд', max_length=64)
    car_types = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    car_type = models.IntegerField(verbose_name='Кузов', choices=car_types)