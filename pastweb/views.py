from django.shortcuts import render
from .models import Pastweb

def web(request):
        webs = Pastweb.objects
        return render(request, 'pastweb/web.html', {'webs' : webs})
