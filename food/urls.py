from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('pizza/', views.pizza, name='pizza'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name= 'service'),
    path('contacts/', views.contact, name='contacts'),
    path('about/', views.about, name='about')
]
