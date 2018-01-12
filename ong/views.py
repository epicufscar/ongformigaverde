from datetime import datetime
import dateutil.relativedelta
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
    periodStart = None
    periodEnd = None

    if request.method == 'POST':
        periodStart = request.POST['period-start']
        periodEnd = request.POST['period-end']
    else:
        periodStart = (datetime.now() + dateutil.relativedelta.relativedelta(years=-1)).strftime('%d/%m/%Y')
        periodEnd = datetime.now().strftime('%d/%m/%Y')

    print(periodStart)
    print(periodEnd)

    p1_valor = 0
    p2_valor = 0
    p3_valor = 0
    p4_valor = 0
    p5_valor = 0
    p6_valor = 0
    p7_valor = 0

    p1_quantidade = 0
    p2_quantidade = 0
    p3_quantidade = 0
    p4_quantidade = 0
    p5_quantidade = 0
    p6_quantidade = 0
    p7_quantidade = 0

    for receita in ReceitaDeDoacoes.objects.all():
        if datetime.strptime(periodStart, '%d/%m/%Y').date() <= receita.data <= datetime.strptime(periodEnd, '%d/%m/%Y').date():
            if receita.utilizacao == 'P1':
                p1_valor += receita.valor
                p1_quantidade += 1

            if receita.utilizacao == 'P2':
                p2_valor += receita.valor
                p2_quantidade += 1

            if receita.utilizacao == 'P3':
                p3_valor += receita.valor
                p3_quantidade += 1

            if receita.utilizacao == 'P4':
                p4_valor += receita.valor
                p4_quantidade += 1

            if receita.utilizacao == 'P5':
                p5_valor += receita.valor
                p5_quantidade += 1

            if receita.utilizacao == 'P6':
                p6_valor += receita.valor
                p6_quantidade += 1

            if receita.utilizacao == 'P7':
                p7_valor += receita.valor
                p7_quantidade += 1

    data = {
        'periodStart': periodStart,
        'periodEnd': periodEnd,
        'chart': {
            'p1_valor': p1_valor,
            'p1_quantidade': p1_quantidade,
            'p2_valor': p2_valor,
            'p2_quantidade': p2_quantidade,
            'p3_valor': p3_valor,
            'p3_quantidade': p3_quantidade,
            'p4_valor': p4_valor,
            'p4_quantidade': p4_quantidade,
            'p5_valor': p5_valor,
            'p5_quantidade': p5_quantidade,
            'p6_valor': p6_valor,
            'p6_quantidade': p6_quantidade,
            'p7_valor': p7_valor,
            'p7_quantidade': p7_quantidade
        }
    }
    return render(request, 'ong/transparencia.html', data)


def noticias(request):
    data = {
        'noticias': Noticia.objects.all().order_by('-data')
    }
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
    projeto = Projeto.objects.get(id=id)

    if projeto.linkVideo.__contains__('youtube'):
        projeto.isYoutube = True
        projeto.youtubeEmbed = projeto.linkVideo.replace('watch?v=', 'embed/')
        projeto.linkVideo = projeto.linkVideo.replace('youtube.com', 'youtu.be')
        projeto.linkVideo = projeto.linkVideo.replace('watch?v=', '')
        projeto.linkVideo = projeto.linkVideo.replace('www.', '')

    elif projeto.linkVideo.__contains__('facebook'):
        projeto.isFacebook = True
        projeto.facebookEmbed = projeto.linkVideo
        projeto.linkVideo = projeto.linkVideo.replace('facebook.com', 'fb.com')
        projeto.linkVideo = projeto.linkVideo.replace('www.', '')

    if projeto.linkFotos.__contains__('facebook'):
        projeto.facebookAlbum = projeto.linkFotos
        projeto.linkFotos = projeto.linkFotos.replace('facebook.com', 'fb.com')
        projeto.linkFotos = projeto.linkFotos.replace('www.', '')

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
        'depoimentos': DepoimentoSobreProjeto.objects.filter(projeto=projeto),
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'proximo': next,
        'anterior': previous
    }
    return render(request, 'ong/projeto.html', data)