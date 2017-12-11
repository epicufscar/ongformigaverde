from django.shortcuts import render
from django.core.mail import send_mail
from .models import *


def home(request):
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'projetos_andamento': Projeto.objects.filter(dataFim=None).count(),
        'parceiros': Parceria.objects.count(),
        'intercambistas': Membro.objects.exclude(pais='BRASIL').count(),
        'projetos': Projeto.objects.all(),
        'campanha_doacao': CampanhaParaDoacoes.objects.all(),
        'email_success': None
    }
    
    if request.method == 'POST':
        name = request.POST['name']
        email = str(name).title() + " <" + request.POST['email'] + ">"
        subject = "[VIA SITE] " + request.POST['subject']
        content = request.POST['message'] + '\n\n----- \n' + name + '\n' + email

        response = send_mail(subject, content, email, [data['informacoes_ong'].email])

        data['email_success'] = response == 1

    return render(request, 'ong/home/home.html', data)

  
def historia(request):
    data = {}
    return render(request, 'ong/historia.html', data)


def missao(request):
    data = {}
    return render(request, 'ong/missao.html', data)


def equipe(request):
    data = {}
    return render(request, 'ong/equipe.html', data)


def parceiros(request):
    data = {}
    return render(request, 'ong/parceiros.html', data)


def projetos(request):
    data = {}
    return render(request, 'ong/projetos.html', data)


def doacoes(request):
    data = {}
    return render(request, 'ong/doacoes.html', data)


def transparencia(request):
    data = {}
    return render(request, 'ong/transparencia.html', data)


def noticias(request):
    data = {}
    return render(request, 'ong/noticias.html', data)


def projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    try:
        previous = projeto.get_previous_by_dataInicio()
    except Projeto.DoesNotExist:
        previous = None

    try:
        next = projeto.get_next_by_dataInicio()
    except Projeto.DoesNotExist:
        next = None

    data = {
        'projeto': projeto,
        'depoimentos': DepoimentoSobreProjeto.objects.all(),
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'proximo': next,
        'anterior': previous
    }
    return render(request, 'ong/projeto.html', data)