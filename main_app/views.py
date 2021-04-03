from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Drink, Drinker
from .form import PouringForm


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


def drink_detail(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    drinker_drink_doesnt_have = Drinker.objects.exclude(
        id__in=drink.drinker.all().values_list('id'))
    pouring_form = PouringForm()
    return render(request, 'drinks/detail.html', {
        'drink': drink,
        'pouring_form': pouring_form,
        'drinker': drinker_drink_doesnt_have
    })


def add_pouring(request, drink_id):
    form = PouringForm(request.POST)
    if form.is_valid():
        new_pouring = form.save(commit=False)
        new_pouring.drink_id = drink_id
        new_pouring.save()
    return redirect('detail', drink_id=drink_id)


def assoc_drinker(request, drink_id, drinker_id):
    Drink.objects.get(id=drink_id).drinker.add(drinker_id)
    return redirect('detail', drink_id=drink_id)


class DrinkCreate(CreateView):
    model = Drink
    fields = '__all__'


class DrinkUpdate(UpdateView):
    model = Drink
    fields = '__all__'


class DrinkDelete(DeleteView):
    model = Drink
    success_url = '/drinks/'
