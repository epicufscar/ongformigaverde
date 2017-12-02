from django.shortcuts import render
from .models import *

def home(request):
    data = {
        'projetos': Projeto.objects.all()
    }
    return render(request, 'ong/home/home.html', data)

