from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.
def index(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def pizza(request):
  template = loader.get_template('pizza.html')
  return HttpResponse(template.render())

def Burger(request):
  template = loader.get_template('Burger.html')
  return HttpResponse(template.render())

def services(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())