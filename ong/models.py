from django.db import models


class Membro(models.Model):
    class Meta:
        verbose_name = 'membro'
        verbose_name_plural = 'membros'

    def __str__(self):
        return '[' + self.pais + '] ' + self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.pais = self.pais.upper()
        self.atividade = self.atividade.upper()
        self.pais_ingles = self.pais_ingles.upper()
        self.atividade_ingles = self.atividade_ingles.upper()
        super(Membro, self).save(*args, **kwargs)

    nome = models.CharField(blank=False, max_length=100, verbose_name='nome')
    email = models.EmailField(blank=True, unique=True, max_length=100, verbose_name='email')
    telefone = models.CharField(blank=True, max_length=20, verbose_name='telefone')
    facebook = models.CharField(blank=True, max_length=100, verbose_name='facebook')
    pais = models.CharField(blank=False, max_length=100, verbose_name='país')
    dataInicio = models.DateField(blank=False, verbose_name='data de início das atividades')
    dataFim = models.DateField(blank=True, null=True, verbose_name='data de término das atividades')
    atividade = models.CharField(blank=False, max_length=100, verbose_name='atividade ou função')
    depoimento = models.TextField(blank=True, verbose_name='depoimento')
    # informacoes que precisam ser traduzidas
    pais_ingles = models.CharField(blank=True, max_length=100, verbose_name='país em inglês')
    atividade_ingles = models.CharField(blank=True, max_length=100, verbose_name='atividade ou função em inglês')
    depoimento_ingles = models.TextField(blank=True, verbose_name='depoimento em inglês')
