from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Drink


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def drinks_index(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/index.html', {'drinks': drinks})


def detail(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    return render(request, 'drinks/detail.html', {'drink': drink})
