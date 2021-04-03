from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Drink, Drinker
from .form import PouringForm


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


@login_required
def drinks_index(request):
    drinks = Drink.objects.filter(user=request.user)
    return render(request, 'drinks/index.html', {'drinks': drinks})


@login_required
def detail(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    return render(request, 'drinks/detail.html', {'drink': drink})


@login_required
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


@login_required
def add_pouring(request, drink_id):
    form = PouringForm(request.POST)
    if form.is_valid():
        new_pouring = form.save(commit=False)
        new_pouring.drink_id = drink_id
        new_pouring.save()
    return redirect('detail', drink_id=drink_id)


@login_required
def assoc_drinker(request, drink_id, drinker_id):
    Drink.objects.get(id=drink_id).drinker.add(drinker_id)
    return redirect('detail', drink_id=drink_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class DrinkCreate(LoginRequiredMixin, CreateView):
    model = Drink
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DrinkUpdate(LoginRequiredMixin, UpdateView):
    model = Drink
    fields = '__all__'


class DrinkDelete(LoginRequiredMixin, DeleteView):
    model = Drink
    success_url = '/drinks/'
