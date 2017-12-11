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
        'noticias': Noticia.objects.order_by('-data')[:10],
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
    data = {
        'projetos': Projeto.objects.all(),
        'campanha_doacao': CampanhaParaDoacoes.objects.all(),
        'criancas': None,
        'adultos': None,
        'todos': None
    }

    data['criancas'] = [p for p in data['projetos'] if p.publico == "P1"]
    data['adultos'] = [p for p in data['projetos'] if p.publico == "P2"]
    data['todos'] = [p for p in data['projetos'] if p.publico == "P3"]

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


def noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    if noticia.linkVideo.__contains__('youtube'):
        noticia.isYoutube = True
        noticia.youtubeEmbed = noticia.linkVideo.replace('watch?v=', 'embed/')
        noticia.linkVideo = noticia.linkVideo.replace('youtube.com', 'youtu.be')
        noticia.linkVideo = noticia.linkVideo.replace('watch?v=', '')
        noticia.linkVideo = noticia.linkVideo.replace('www.', '')

    elif noticia.linkVideo.__contains__('facebook'):
        noticia.isFacebook = True
        noticia.facebookEmbed = noticia.linkVideo
        noticia.linkVideo = noticia.linkVideo.replace('facebook.com', 'fb.com')
        noticia.linkVideo = noticia.linkVideo.replace('www.', '')

    if noticia.linkFotos.__contains__('facebook'):
        noticia.facebookAlbum = noticia.linkFotos
        noticia.linkFotos = noticia.linkFotos.replace('facebook.com', 'fb.com')
        noticia.linkFotos = noticia.linkFotos.replace('www.', '')

    try:
        next = noticia.get_next_by_data()
    except Noticia.DoesNotExist:
        next = None

    try:
        previous = noticia.get_previous_by_data()
    except Noticia.DoesNotExist:
        previous = None

    data = {
        'noticia': noticia,
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'proxima': next,
        'anterior': previous
    }
    return render(request, 'ong/noticia.html', data)


def projeto(request, id):
    data = {
        'projeto': Projeto.objects.get(id = id),
        'depoimentos': DepoimentoSobreProjeto.objects.all()
    }
    return render(request, 'ong/projeto.html', data)
