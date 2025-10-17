# taxi/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    """
    Кастомна модель користувача (Driver), що наслідує AbstractUser
    та додає поле license_number.
    """
    license_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.license_number})"


class Manufacturer(models.Model):
    """
    Виробник автомобіля. name повинен бути унікальним.
    """
    name = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    """
    Автомобіль — має модель, зв'язок з виробником та водіїв (many-to-many).
    """
    model = models.CharField(max_length=128)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name='cars', blank=True)

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"
