from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def drinks_index(request):
    return render(request, 'drinks/index.html', {'drinks': drinks})


class Drink:
    def __init__(self, name, brand, size):
        self.name = name
        self.brand = brand
        self.size = size


drinks = [
    Drink('Coca-Cola', 'The Coca-Cola Company', '355 mL'),
    Drink('Pepsi', 'PepsiCo', '355 mL'),
    Drink('Sprite', 'The Coca-Cola Company', '500 mL'),
    Drink('Fanta', 'The Coca-Cola Company', '500 mL'),
]
