from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class DrinkCreate(CreateView):
    model = Drink
    fields = '__all__'


class DrinkUpdate(UpdateView):
    model = Drink
    fields = '__all__'


class DrinkDelete(DeleteView):
    model = Drink
    success_url = '/drinks/'
