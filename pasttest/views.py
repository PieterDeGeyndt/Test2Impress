from django.shortcuts import render
from .models import Pasttest

def test(request):
    projects=Pasttest.objects.order_by("-teststart")
    return render(request, 'pasttest/test.html', {'projects' : projects})

def timeline(request):
    projects=Pasttest.objects.order_by("-teststart")
    return render(request, 'pasttest/timeline.html', {'projects' : projects})