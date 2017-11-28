from django.contrib import admin
from .models import *


class MembroAdmin(admin.ModelAdmin):
    exclude = ('photo64', 'possuiPhoto')
    readonly_fields = ('photo64', 'possuiPhoto')
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


admin.site.register(Membro, MembroAdmin)
admin.site.register(Projeto)
admin.site.register(CampanhaParaDoacoes)
admin.site.register(DepoimentoSobreProjeto)
admin.site.register(Parceria)
admin.site.register(ReceitaDeDoacoes)
admin.site.register(Noticia)
