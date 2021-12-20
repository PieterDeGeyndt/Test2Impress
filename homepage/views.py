from django.shortcuts import render
from .models import Homepage

def home(request):
        homeinfo = Homepage.objects
        return render(request, 'homepage/home.html', {'homeinfo' : homeinfo})
