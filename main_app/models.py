from django.db import models
from django.urls import reverse

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})
