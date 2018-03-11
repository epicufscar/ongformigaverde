from datetime import datetime
import dateutil.relativedelta
from django.shortcuts import render
from django.core.mail import send_mail
from .models import *


def home(request):
    projetos = Projeto.objects.all()
    campanhas = CampanhaParaDoacoes.objects.all()
    campanhasPrimeiro = []

    for projeto in projetos:
        if campanhas.filter(projeto=projeto):
                campanhasPrimeiro.insert(0, projeto)
        else:
            campanhasPrimeiro.append(projeto)

    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'projetos_andamento': Projeto.objects.filter(dataFim=None).count(),
        'parceiros': Parceria.objects.count(),
        'intercambistas': Membro.objects.exclude(pais='BRASIL').count(),
        'projetos': campanhasPrimeiro,
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
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first()
    }
    return render(request, 'ong/historia.html', data)


def missao(request):
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
    }
    return render(request, 'ong/missao.html', data)


def equipe(request):
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'membros': Membro.objects.all()
    }
    return render(request, 'ong/equipe.html', data)


def parceiros(request):
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'parceiros': Parceria.objects.all(),
        'comunidades': None,
        'universiades': None,
        'empresas': None
    }

    data['comunidades'] = [p for p in data['parceiros'] if p.tipo == "P1"]
    data['universidades'] = [p for p in data['parceiros'] if p.tipo == "P2"]
    data['empresas'] = [p for p in data['parceiros'] if p.tipo == "P3"]

    return render(request, 'ong/parceiros.html', data)


def projetos(request):
    projetos = Projeto.objects.all()
    campanhas = CampanhaParaDoacoes.objects.all()
    campanhasPrimeiro = []

    for projeto in projetos:
        if campanhas.filter(projeto=projeto):
            campanhasPrimeiro.insert(0, projeto)
        else:
            campanhasPrimeiro.append(projeto)

    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'projetos': campanhasPrimeiro,
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
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first()
    }
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

    p_valor = [0, 0, 0, 0, 0, 0, 0]
    p_quantidade = [0, 0, 0, 0, 0, 0, 0]
    receitas = []
    campanhas = CampanhaParaDoacoes.objects.order_by('-dataFim')

    for receita in ReceitaDeDoacoes.objects.order_by('-data'):
        if datetime.strptime(periodStart, '%d/%m/%Y').date() <= receita.data <= datetime.strptime(periodEnd, '%d/%m/%Y').date():
            if receita.utilizacao == 'P1':
                receita.utilizacaoT = 'Manutenção administrativa da ONG'
                receita.utilizacaoEn = 'Administration and maintenance tasks'
                p_valor[0] += receita.valor
                p_quantidade[0] += 1

            if receita.utilizacao == 'P2':
                receita.utilizacaoT = 'Aplicação em projetos existentes'
                receita.utilizacaoEn = 'Investments in existing projects'
                p_valor[1] += receita.valor
                p_quantidade[1] += 1

            if receita.utilizacao == 'P3':
                receita.utilizacaoT = 'Criação de novos projetos'
                receita.utilizacaoEn = 'Creation of new projects'
                p_valor[2] += receita.valor
                p_quantidade[2] += 1

            if receita.utilizacao == 'P4':
                receita.utilizacaoT = 'Aquisição de recursos e materiais'
                receita.utilizacaoEn = 'Resources and materials acquisition'
                p_valor[3] += receita.valor
                p_quantidade[3] += 1

            if receita.utilizacao == 'P5':
                receita.utilizacaoT = 'Treinamentos para membros da equipe'
                receita.utilizacaoEn = 'Training of team members'
                p_valor[4] += receita.valor
                p_quantidade[4] += 1

            if receita.utilizacao == 'P6':
                receita.utilizacaoT = 'Eventos e comemorações'
                receita.utilizacaoEn = 'Events and celebrations'
                p_valor[5] += receita.valor
                p_quantidade[5] += 1

            if receita.utilizacao == 'P7':
                receita.utilizacaoT = 'Outras finalidades'
                receita.utilizacaoEn = 'Other demands'
                p_valor[6] += receita.valor
                p_quantidade[6] += 1

            receita.data = receita.data.strftime('%d/%b/%Y')
            receitas.append(receita)

    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
        'campanhas': campanhas,
        'receitas': receitas,
        'periodStart': periodStart,
        'periodEnd': periodEnd,
        'chart': {
            'p_valor': p_valor,
            'p_quantidade': p_quantidade
        }
    }
    return render(request, 'ong/transparencia.html', data)


def noticias(request):
    data = {
        'informacoes_ong': InformacoesGeraisONG.objects.first(),
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
