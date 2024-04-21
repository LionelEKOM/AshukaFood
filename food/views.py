from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.
def index(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def pizza(request):
  template = loader.get_template('pizza.html')
  return HttpResponse(template.render())

def Burger(request):
  template = loader.get_template('Burger.html')
  return HttpResponse(template.render())
def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def services(request):
  template = loader.get_template('demo.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())