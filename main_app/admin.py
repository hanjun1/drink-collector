from django.contrib import admin
from .models import Drink, Pouring, Drinker
# Register your models here.

admin.site.register(Drink)
admin.site.register(Pouring)
admin.site.register(Drinker)
