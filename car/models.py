from django.db import models


class Car(models.Model):
    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
