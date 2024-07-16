from django.shortcuts import render
from .models import Register

# Create your views here.

def register(request):
    return render(request, 'register.html', {'users': Register.objects.all()})

def userPage(request, id):
    return render(request, 'user.html', {'user': Register.objects.get(id=id)})
