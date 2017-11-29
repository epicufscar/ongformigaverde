from django.shortcuts import render
from .models import *


def home(request):
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first()
    }
    return render(request, 'ong/home/home.html', data)

