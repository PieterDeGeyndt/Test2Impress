from django.shortcuts import render
from .models import Pasttest

def test(request):
    projects=Pasttest.objects
    return render(request, 'homepage/home.html', {'projecs' : projects})