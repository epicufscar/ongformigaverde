from django.db import models


class Membro(models.Model):
    class Meta:
        verbose_name = 'membro'
        verbose_name_plural = 'membros'
        ordering = ['pais']

    def __str__(self):
        return '[' + self.pais + '] ' + self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.pais = self.pais.upper()
        self.atividade = self.atividade.upper()
        self.country = self.country.upper()
        self.activity = self.activity.upper()
        super(Membro, self).save(*args, **kwargs)

    nome = models.CharField(blank=False, max_length=100, verbose_name='nome')
    email = models.EmailField(blank=True, unique=True, max_length=100, verbose_name='email')
    telefone = models.CharField(blank=True, max_length=20, verbose_name='telefone')
    facebook = models.CharField(blank=True, max_length=100, verbose_name='facebook')
    pais = models.CharField(blank=False, max_length=100, verbose_name='país')
    dataInicio = models.DateField(blank=False, verbose_name='data de início das atividades')
    dataFim = models.DateField(blank=True, null=True, verbose_name='data de término das atividades, se houver')
    atividade = models.CharField(blank=False, max_length=100, verbose_name='atividade ou função')
    depoimento = models.TextField(blank=True, verbose_name='depoimento')
    # informacoes que precisam ser traduzidas
    country = models.CharField(blank=True, max_length=100, verbose_name='[INGLÊS] País em inglês')
    activity = models.CharField(blank=True, max_length=100, verbose_name='[INGLÊS] Atividade ou função em inglês')
    statement = models.TextField(blank=True, verbose_name='[INGLÊS] Depoimento em inglês')


class Projeto(models.Model):
    class Meta:
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.name = self.name.upper()
        super(Projeto, self).save(*args, **kwargs)

    PUBLICO = (
        ('P1', 'CRIANÇAS'),
        ('P2', 'ADULTOS'),
        ('P3', 'TODOS')
    )

    PUBLIC = (
        ('E1', 'CHILDREN'),
        ('E2', 'ADULTS'),
        ('E3', 'EVERYONE')
    )

    nome = models.CharField(blank=False, max_length=100, verbose_name='nome')
    descricao = models.TextField(blank=False, verbose_name='descrição')
    publico = models.CharField(blank=False, max_length=2, choices=PUBLICO, verbose_name='público alvo')
    dataInicio = models.DateField(blank=False, verbose_name='data de início do projeto')
    dataFim = models.DateField(blank=True, null=True, verbose_name='data de término do projeto, se houver')
    linkFotos = models.URLField(blank=True, verbose_name='link para álbum de fotos do projeto')
    linkVideo = models.URLField(blank=True, verbose_name='link para vídeo do projeto')
    membros = models.ManyToManyField(Membro, blank=True, verbose_name='membros responsáveis pelo projeto')
    # informacoes que precisam ser traduzidas
    name = models.CharField(blank=True, max_length=100, verbose_name='[INGLÊS] Nome em inglês')
    description = models.TextField(blank=True, verbose_name='[INGLÊS] Descrição em inglês')
    public = models.CharField(blank=True, max_length=2, choices=PUBLIC, verbose_name='[INGLÊS] Público alvo em inglês')


class CampanhaParaDoacoes(models.Model):
    class Meta:
        verbose_name = 'campanha para doação'
        verbose_name_plural = 'campanha para doações'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.titulo = self.titulo.upper()
        self.title = self.title.upper()
        super(CampanhaParaDoacoes, self).save(*args, **kwargs)

    titulo = models.CharField(blank=False, max_length=100, verbose_name='título')
    descricao = models.TextField(blank=False, verbose_name='descrição')
    link = models.URLField(blank=False, verbose_name='link para campanha (onde o dinheiro é arrecadado)')
    projeto = models.ForeignKey(Projeto, blank=False, verbose_name='projeto para o qual a campanha foi criada')
    dataInicio = models.DateField(blank=False, verbose_name='data de início da campanha')
    dataFim = models.DateField(blank=True, null=True,
                               verbose_name='data de término da campanha (até quando o link fica disponível no site)')
    # informacoes que precisam ser traduzidas
    title = models.CharField(blank=True, max_length=100, verbose_name='[INGLÊS] Título em inglês')
    description = models.TextField(blank=True, verbose_name='[INGLÊS] Descrição em inglês')


class DepoimentoSobreProjeto(models.Model):
    class Meta:
        verbose_name = 'depoimento sobre projeto'
        verbose_name_plural = 'depoimentos sobre projeto'
        ordering = ['projeto__nome']

    def __str__(self):
        return '[' + self.projeto.nome + '] ' + self.nome

    def save(self, *args, **kwargs):
        super(DepoimentoSobreProjeto, self).save(*args, **kwargs)

    nome = models.CharField(blank=False, max_length=100, verbose_name='nome de quem fez o depoimento')
    idade = models.PositiveIntegerField(blank=True, verbose_name='idade de quem fez o depoimento')
    depoimento = models.TextField(blank=False, verbose_name='depoimento')
    linkVideo = models.URLField(blank=True, verbose_name='link para depoimento em vídeo')
    projeto = models.ForeignKey(Projeto, blank=False, verbose_name='projeto para o qual o depoimento foi feito')
    # informacoes que precisam ser traduzidas
    statement = models.TextField(blank=True, verbose_name='[INGLÊS] Depoimento em inglês')

