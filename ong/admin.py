from django.contrib import admin
from .models import *


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


admin.site.register(Membro, MembroAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(CampanhaParaDoacoes, CampanhaParaDoacoesAdmin)
admin.site.register(DepoimentoSobreProjeto, DepoimentoSobreProjetoAdmin)
admin.site.register(Parceria, ParceriaAdmin)
admin.site.register(ReceitaDeDoacoes, ReceitaDeDoacoesAdmin)
admin.site.register(Noticia, NoticiaAdmin)
