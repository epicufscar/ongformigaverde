from django.db import models
from django.dispatch import receiver


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

        if self.photo64:
            self.possuiPhoto = True

        if self.apagarPhoto:
            self.photo = None
            self.photo64 = None
            self.possuiPhoto = False

        self.apagarPhoto = False
        super(Membro, self).save(*args, **kwargs)

    nome = models.CharField(blank=False, max_length=100, verbose_name='nome completo')
    email = models.EmailField(blank=True, max_length=100, verbose_name='email')
    telefone = models.CharField(blank=True, max_length=20, verbose_name='telefone')
    facebook = models.CharField(blank=True, max_length=100, verbose_name='facebook')
    pais = models.CharField(blank=False, max_length=100, verbose_name='país')
    dataInicio = models.DateField(blank=False, verbose_name='data de início das atividades')
    dataFim = models.DateField(blank=True, null=True, verbose_name='data de término das atividades', help_text='Preencher, se houver')
    atividade = models.CharField(blank=True, max_length=100, verbose_name='atividade', help_text='Atividade ou função que este membro exerce na ONG')
    depoimento = models.TextField(blank=True, verbose_name='depoimento sobre a ONG')
    photo = models.ImageField(null=True, blank=True, upload_to='ong/static/images/', verbose_name='foto', help_text='Utilize este campo para carregar uma nova foto ou substituir foto existente')
    photo64 = models.TextField(null=True, editable=False)
    possuiPhoto = models.BooleanField(blank=True, default=False, verbose_name='possui foto?')
    apagarPhoto = models.BooleanField(blank=True, default=False, verbose_name='excluir foto?', help_text='Marque esta opção apenas se deseja excluir a foto ao salvar')
    # informacoes que precisam ser traduzidas
    country = models.CharField(blank=True, max_length=100, verbose_name='país, em inglês')
    activity = models.CharField(blank=True, max_length=100, verbose_name='atividade, em inglês', help_text='Atividade ou função que este membro exerce na ONG')
    statement = models.TextField(blank=True, verbose_name='depoimento sobre a ONG, em inglês')


class Parceria(models.Model):
    class Meta:
        verbose_name = 'parceria'
        verbose_name_plural = 'parcerias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.responsavel = self.responsavel.upper()
        self.endereco = self.endereco.upper()

        if self.photo64:
            self.possuiPhoto = True

        if self.apagarPhoto:
            self.photo = None
            self.photo64 = None
            self.possuiPhoto = False

        self.apagarPhoto = False
        super(Parceria, self).save(*args, **kwargs)

    TIPO = (
        ('P1', 'COMUNIDADE'),
        ('P2', 'UNIVERSIDADE'),
        ('P3', 'EMPRESA')
    )

    TYPE = (
        ('E1', 'COMMUNITY'),
        ('E2', 'UNIVERSITY'),
        ('E3', 'COMPANY')
    )

    nome = models.CharField(blank=False, max_length=100, verbose_name='nome do parceiro', help_text='Exemplo: USP ou UFSCar')
    responsavel = models.CharField(blank=True, max_length=100, verbose_name='responsável', help_text='Nome do responsável ou pessoa para contato principal (Exemplo: João Augusto)')
    telefone = models.CharField(blank=True, max_length=20, verbose_name='telefone do parceiro', help_text='Telefone principal para contato com o parceiro')
    endereco = models.CharField(blank=True, max_length=300, verbose_name='endereço do parceiro')
    link = models.URLField(blank=True, verbose_name='link para site ou página do parceiro')
    tipo = models.CharField(blank=False, max_length=2, choices=TIPO, verbose_name='tipo')
    photo = models.ImageField(null=True, blank=True, upload_to='ong/static/images/', verbose_name='foto', help_text='Utilize este campo para carregar uma nova foto ou substituir foto existente')
    photo64 = models.TextField(null=True, editable=False)
    possuiPhoto = models.BooleanField(blank=True, default=False, verbose_name='possui foto?')
    apagarPhoto = models.BooleanField(blank=True, default=False, verbose_name='excluir foto?', help_text='Marque esta opção apenas se deseja excluir a foto ao salvar')
    # informacoes que precisam ser traduzidas
    type = models.CharField(blank=False, max_length=2, choices=TYPE, verbose_name='tipo, em inglês')


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

        if self.photo64:
            self.possuiPhoto = True

        if self.apagarPhoto:
            self.photo = None
            self.photo64 = None
            self.possuiPhoto = False

        self.apagarPhoto = False
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

    nome = models.CharField(blank=False, max_length=100, verbose_name='nome do projeto')
    descricao = models.TextField(blank=False, verbose_name='descrição')
    publico = models.CharField(blank=False, max_length=2, choices=PUBLICO, verbose_name='público alvo')
    dataInicio = models.DateField(blank=False, verbose_name='data de início do projeto')
    dataFim = models.DateField(blank=True, null=True, verbose_name='data de término do projeto', help_text='Preencher, se houver')
    linkFotos = models.URLField(blank=True, verbose_name='link para álbum de fotos do projeto')
    linkVideo = models.URLField(blank=True, verbose_name='link para vídeo do projeto')
    membros = models.ManyToManyField(Membro, blank=True, verbose_name='membros', help_text='Membros responsáveis pelo projeto, se houver.')
    parceiros = models.ManyToManyField(Parceria, blank=True, verbose_name='parceiros', help_text='Parceiros envolvidos com o projeto, se houver.')
    photo = models.ImageField(null=True, blank=True, upload_to='ong/static/images/', verbose_name='foto de capa do projeto', help_text='Utilize este campo para carregar uma nova foto ou substituir foto existente')
    photo64 = models.TextField(null=True, editable=False)
    possuiPhoto = models.BooleanField(blank=True, default=False, verbose_name='possui foto de capa?')
    apagarPhoto = models.BooleanField(blank=True, default=False, verbose_name='excluir foto de capa?', help_text='Marque esta opção apenas se deseja excluir a foto de capa ao salvar')
    # informacoes que precisam ser traduzidas
    name = models.CharField(blank=True, max_length=100, verbose_name='nome do projeto, em inglês')
    description = models.TextField(blank=True, verbose_name='descrição, em inglês')
    public = models.CharField(blank=False, max_length=2, choices=PUBLIC, verbose_name='público alvo, em inglês')


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

    titulo = models.CharField(blank=False, max_length=100, verbose_name='título da campanha')
    descricao = models.TextField(blank=False, verbose_name='descrição')
    link = models.URLField(blank=False, verbose_name='link para campanha', help_text='Onde o dinheiro será arrecadado')
    projeto = models.ForeignKey(Projeto, null=True, blank=True, verbose_name='projeto', help_text='Projeto para o qual a campanha foi criada, se aplicável')
    dataInicio = models.DateField(blank=False, verbose_name='data de início da campanha')
    dataFim = models.DateField(blank=True, null=True, verbose_name='data de término da campanha', help_text='Até quando o link fica disponível no site?')
    # informacoes que precisam ser traduzidas
    title = models.CharField(blank=True, max_length=100, verbose_name='título, em inglês')
    description = models.TextField(blank=True, verbose_name='descrição, em inglês')


class DepoimentoSobreProjeto(models.Model):
    class Meta:
        verbose_name = 'depoimento sobre projeto'
        verbose_name_plural = 'depoimentos sobre projeto'
        ordering = ['projeto__nome']

    def __str__(self):
        return '[' + self.projeto.nome + '] ' + self.nome

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()

        if self.photo64:
            self.possuiPhoto = True

        if self.apagarPhoto:
            self.photo = None
            self.photo64 = None
            self.possuiPhoto = False

        self.apagarPhoto = False
        super(DepoimentoSobreProjeto, self).save(*args, **kwargs)

    nome = models.CharField(blank=False, max_length=100, verbose_name='nome', help_text='Nome de quem fez o depoimento')
    idade = models.PositiveIntegerField(blank=True, verbose_name='idade', help_text='Idade de quem fez o depoimento')
    depoimento = models.TextField(blank=False, verbose_name='depoimento sobre projeto')
    linkVideo = models.URLField(blank=True, verbose_name='link para vídeo', help_text='Link para depoimento em vídeo, se houver')
    projeto = models.ForeignKey(Projeto, blank=False, verbose_name='projeto', help_text='Projeto para o qual o depoimento foi feito')
    photo = models.ImageField(null=True, blank=True, upload_to='ong/static/images/', verbose_name='foto', help_text='Foto de quem fez o depoimento, se houver. Utilize este campo para carregar uma nova foto ou substituir foto existente')
    photo64 = models.TextField(null=True, editable=False)
    possuiPhoto = models.BooleanField(blank=True, default=False, verbose_name='possui foto?')
    apagarPhoto = models.BooleanField(blank=True, default=False, verbose_name='excluir foto?', help_text='Marque esta opção apenas se deseja excluir a foto ao salvar')
    # informacoes que precisam ser traduzidas
    statement = models.TextField(blank=True, verbose_name='depoimento sobre projeto, em inglês')


class ReceitaDeDoacoes(models.Model):
    class Meta:
        verbose_name = 'receita de doações'
        verbose_name_plural = 'receitas de doações'
        ordering = ['valor']

    def __str__(self):
        return '[' + str(self.data) + '] ' + str(self.valor)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super(ReceitaDeDoacoes, self).save(*args, **kwargs)

    UTILIZACAO = (
        ('P1', 'Manutenção administrativa da ONG'),
        ('P2', 'Aplicação em projetos existentes'),
        ('P3', 'Criação de novos projetos'),
        ('P4', 'Aquisição de recursos e materiais'),
        ('P5', 'Treinamentos para membros da equipe'),
        ('P6', 'Eventos e comemorações'),
        ('P7', 'Outras finalidades'),
    )

    USAGE = (
        ('E1', 'Administration and maintenance tasks'),
        ('E2', 'Investments on existing projects'),
        ('E3', 'Creation of new projects'),
        ('E4', 'Resources and materials acquisition'),
        ('E5', 'Training of team members'),
        ('E6', 'Events and celebrations'),
        ('E7', 'Other demands'),
    )

    MEIO_PGTO = (
        ('PM1', 'PayPal'),
        ('PM2', 'Vakinha'),
        ('PM3', 'Boleto'),
        ('PM4', 'Depósito Bancário'),
        ('PM5', 'Transferência Bancária'),
        ('PM5', 'Dinheiro'),
        ('PM7', 'Outro')
    )

    PAY_METHOD = (
        ('EM1', 'PayPal'),
        ('EM2', 'Vakinha'),
        ('EM3', 'Boleto'),
        ('EM4', 'Bank Deposit'),
        ('EM5', 'Bank Transfer'),
        ('EM5', 'Cash'),
        ('EM7', 'Other')
    )

    data = models.DateField(blank=False, verbose_name='data da doação')
    valor = models.FloatField(blank=False, verbose_name='valor da doação')
    anonimo = models.BooleanField(blank=False, verbose_name='doação anônima?', help_text='Marque este campo apenas se esta foi uma doação anônima; deixe em branco caso contrário)')
    nome = models.CharField(blank=True, max_length=100, verbose_name='nome do doador', help_text='Preencha com o nome do doador apenas se a doação não foi anônima, isto é, o doador gostaria de ser reconhecido por isso')
    utilizacao = models.CharField(blank=False, max_length=2, choices=UTILIZACAO, verbose_name='forma de utilização', help_text='Como esse valor foi ou será gasto/utilizado pela ONG?')
    meioPagto = models.CharField(blank=False, max_length=3, choices=MEIO_PGTO, verbose_name='meio de pagamento', help_text='Meio de pagamento utilizado pelo doador')
    comentarios = models.CharField(blank=True, max_length=100, verbose_name='outras informações', help_text='Exemplo: nome do projeto ou evento para o qual o valor foi utilizado')
    # informacoes que precisam ser traduzidas
    usage = models.CharField(blank=False, max_length=2, choices=USAGE, verbose_name='forma de utilização, em inglês', help_text='Como esse valor foi ou será gasto/utilizado pela ONG, em ingles')
    payMethod = models.CharField(blank=False, max_length=3, choices=PAY_METHOD, verbose_name='meio de pagamento, em inglês', help_text='Meio de pagamento utilizado pelo doador')


class Noticia(models.Model):
    class Meta:
        verbose_name = 'notícia'
        verbose_name_plural = 'notícias'

    def __str__(self):
        return '[' + str(self.data) + '] ' + self.titulo

    def save(self, *args, **kwargs):
        self.titulo = self.titulo.capitalize()

        if self.photo64:
            self.possuiPhoto = True

        if self.apagarPhoto:
            self.photo = None
            self.photo64 = None
            self.possuiPhoto = False

        self.apagarPhoto = False
        super(Noticia, self).save(*args, **kwargs)

    data = models.DateField(blank=False, verbose_name='data de postagem', help_text='Corresponde à data que aparecerá no site')
    titulo = models.CharField(blank=False, max_length=100, verbose_name='título da notícia')
    texto = models.TextField(blank=False, verbose_name='texto da notícia')
    link = models.URLField(blank=True, verbose_name='link para conteúdo externo', help_text='Exemplo: link para um post no Facebook ou para um site externo')
    linkFotos = models.URLField(blank=True, verbose_name='link para álbum de fotos da notícia')
    linkVideo = models.URLField(blank=True, verbose_name='link para vídeo sobre a notícia')
    photo = models.ImageField(null=True, blank=True, upload_to='ong/static/images/', verbose_name='foto de capa', help_text='Utilize este campo para carregar uma nova foto ou substituir foto existente')
    photo64 = models.TextField(null=True, editable=False)
    possuiPhoto = models.BooleanField(blank=True, default=False, verbose_name='possui foto de capa?')
    apagarPhoto = models.BooleanField(blank=True, default=False, verbose_name='excluir foto de capa?', help_text='Marque esta opção apenas se deseja excluir a foto de capa ao salvar')


def image_to_b64(image_file):
    import base64
    with open(image_file.path, 'rb') as f:
        encoded_string = base64.b64encode(f.read())
        return encoded_string


@receiver(models.signals.post_save, sender=Membro)
@receiver(models.signals.post_save, sender=Projeto)
@receiver(models.signals.post_save, sender=Parceria)
@receiver(models.signals.post_save, sender=DepoimentoSobreProjeto)
@receiver(models.signals.post_save, sender=Noticia)
def create_base64_str(sender, instance, **kwargs):
    if instance.photo:
        instance.photo64 = image_to_b64(instance.photo)
        instance.photo.delete()
        instance.save()
