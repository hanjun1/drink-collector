from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('drinks/', views.drinks_index, name="drinks"),
    path('drinks/create/', views.DrinkCreate.as_view(), name="drinks_create"),
    path('drinks/<int:drink_id>/', views.drink_detail, name="detail"),
    path('drinks/<int:pk>/edit/', views.DrinkUpdate.as_view(), name="drink_update"),
    path('drinks/<int:pk>/delete/',
         views.DrinkDelete.as_view(), name="drink_delete"),
    path('drinks/<int:drink_id>/add_pouring/',
         views.add_pouring, name='add_pouring'),
    path('drinks/<int:drink_id>/assoc_drinker/<int:drinker_id>/',
         views.assoc_drinker, name="assoc_drinker"),
    path('accounts/signup/', views.signup, name="signup"),
]
