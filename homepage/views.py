from django.shortcuts import render
from .models import Homepage

def home(request):
        homes = Homepage.objects
        return render(request, 'homepage/home.html', {'homes' : homes})

def menu(request):
        return render(request, 'homepage/menu.html')
