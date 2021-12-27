from django.shortcuts import render
from .models import Who

def who(request):
        whos = Who.objects
        return render(request, 'who/who.html', {'whos' : whos})
