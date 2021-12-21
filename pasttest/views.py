from django.shortcuts import render
from .models import Pasttest

def test(request):
    return render(request, 'pasttest/test.html')