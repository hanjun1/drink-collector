from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('drinks/', views.drinks_index, name="drinks"),
    path('drinks/<int:drink_id>/', views.detail, name="detail"),
]
