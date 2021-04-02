from django.db import models
from django.urls import reverse

# Create your models here.


class Drink(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'drink_id': self.id})


class Pouring(models.Model):
    date = models.DateField()
    pour = models.IntegerField()
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return f"Poured {self.pour} mL on {self.date}"

    class Meta:
        ordering = ['date']
