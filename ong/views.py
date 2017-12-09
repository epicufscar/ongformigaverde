from django.shortcuts import render
from .models import *

def home(request):
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'projetos_andamento': Projeto.objects.filter(dataFim=None).count(),
        'parceiros': Parceria.objects.count(),
        'intercambistas': Membro.objects.exclude(pais='BRASIL').count(),
        'projetos': Projeto.objects.all(),
        'campanha_doacao': CampanhaParaDoacoes.objects.all()
    }
    return render(request, 'ong/home/home.html', data)
