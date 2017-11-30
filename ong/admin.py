from django.contrib import admin
import django.contrib.auth.models
from django.contrib import auth
from django.contrib.admin import register
from .models import *

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)

@register(Membro)
class MembroAdmin(admin.ModelAdmin):
    readonly_fields = ('possuiPhoto',)
    list_display = ('nome', 'email', 'pais', 'possuiPhoto',)
    search_fields = ('nome', 'email', 'pais', 'atividade',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'email', 'telefone', 'facebook', 'pais', 'dataInicio', 'dataFim', 'atividade', 'depoimento',)
        }),
        ('Foto de Perfil', {
            'fields': ('photo', 'possuiPhoto', 'apagarPhoto',)
        }),
        ('Em Inglês', {
            'fields': ('country', 'activity', 'statement',)
        })
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(MembroAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['pais'].initial = 'BRASIL'
        form.base_fields['country'].initial = 'BRAZIL'
        return form


@register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    readonly_fields = ('possuiPhoto',)
    list_display = ('nome', 'publico', 'possuiPhoto',)
    search_fields = ('nome', 'publico',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'publico', 'dataInicio', 'dataFim',)
        }),
        ('Mídias', {
            'fields': ('photo', 'possuiPhoto', 'apagarPhoto', 'linkFotos', 'linkVideo',)
        }),
        ('Membros e/ou Parceiros envolvidos', {
            'fields': ('membros', 'parceiros',)
        }),
        ('Em Inglês', {
            'fields': ('name', 'description', 'public',)
        })
    )


@register(Parceria)
class ParceriaAdmin(admin.ModelAdmin):
    readonly_fields = ('possuiPhoto',)
    list_display = ('nome', 'responsavel', 'telefone', 'tipo', 'possuiPhoto',)
    search_fields = ('nome', 'responsavel', 'tipo', 'endereco')
    fieldsets = (
        (None, {
            'fields': ('nome', 'responsavel', 'telefone', 'endereco', 'link', 'tipo',)
        }),
        ('Foto', {
            'fields': ('photo', 'possuiPhoto', 'apagarPhoto',)
        }),
        ('Em Inglês', {
            'fields': ('type',)
        })
    )


@register(CampanhaParaDoacoes)
class CampanhaParaDoacoesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'dataInicio', 'dataFim',)
    search_fields = ('titulo',)
    fieldsets = (
        (None, {
            'fields': ('titulo', 'descricao', 'link', 'projeto', 'dataInicio', 'dataFim',)
        }),
        ('Em Inglês', {
            'fields': ('title', 'description')
        })
    )


@register(DepoimentoSobreProjeto)
class DepoimentoSobreProjetoAdmin(admin.ModelAdmin):
    readonly_fields = ('possuiPhoto',)
    list_display = ('nome', 'idade', 'projeto', 'possuiPhoto',)
    search_fields = ('nome', 'idade',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'idade', 'projeto', 'depoimento',)
        }),
        ('Mídias', {
            'fields': ('photo', 'possuiPhoto', 'apagarPhoto', 'linkVideo',)
        }),
        ('Em Inglês', {
            'fields': ('statement',)
        })
    )


@register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('possuiPhoto',)
    list_display = ('titulo', 'data', 'link', 'possuiPhoto')
    search_fields = ('titulo',)
    fieldsets = (
        (None, {
            'fields': ('data', 'titulo', 'texto',)
        }),
        ('Mídias', {
            'fields': ('photo', 'possuiPhoto', 'apagarPhoto', 'link', 'linkFotos', 'linkVideo',)
        })
    )


@register(ReceitaDeDoacoes)
class ReceitaDeDoacoesAdmin(admin.ModelAdmin):
    list_display = ('data', 'valor', 'anonimo', 'utilizacao', 'meioPagto',)
    search_fields = ('valor', 'utilizacao', 'meioPagto', 'nome',)
    fieldsets = (
        (None, {
            'fields': ('data', 'valor', 'anonimo', 'nome', 'meioPagto',)
        }),
        ('Transparência', {
            'fields': ('utilizacao', 'comentarios',)
        }),
        ('Em Inglês', {
            'fields': ('payMethod', 'usage',)
        })
    )


@register(InformacoesGeraisONG)
class InformacoesGeraisONGAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('nome', 'endereco', 'email', 'telefone',)
    fieldsets = (
        ('Informações de Contato', {
            'fields': ('nome', 'endereco', 'email', 'telefone',)
        }),
        ('Redes Sociais', {
            'fields': ('facebook', 'instagram', 'youtube', 'twitter',)
        }),
        ("Identidade da ONG", {
            'fields': ('missao', 'visao', 'valores', 'principios', 'proverbio',)
        }),
        ("Em Inglês", {
            'fields': ('mission', 'vision', 'values', 'principles', 'proverb',)
        })
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
