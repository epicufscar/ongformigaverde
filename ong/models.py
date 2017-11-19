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
    country = models.CharField(blank=True, max_length=100, verbose_name='país em inglês')
    activity = models.CharField(blank=True, max_length=100, verbose_name='atividade ou função em inglês')
    statement = models.TextField(blank=True, verbose_name='depoimento em inglês')


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
    name = models.CharField(blank=True, max_length=100, verbose_name='nome em inglês')
    description = models.TextField(blank=True, verbose_name='descrição em inglês')
    public = models.CharField(blank=True, max_length=2, choices=PUBLIC, verbose_name='público alvo em inglês')
