from django.shortcuts import render
from .models import Pasttest

def test(request):
    projects=Pasttest.objects
    year=Pasttest.get_year
    return render(request, 'pasttest/test.html', {'projects' : projects}, {'year': year})