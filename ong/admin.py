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


admin.site.register(Membro, MembroAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(CampanhaParaDoacoes)
admin.site.register(DepoimentoSobreProjeto)
admin.site.register(Parceria)
admin.site.register(ReceitaDeDoacoes)
admin.site.register(Noticia)
