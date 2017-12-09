from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^historia/$', historia, name='historia'),
    url(r'^missao/$', missao, name='missao'),
    url(r'^equipe/$', equipe, name='equipe'),
    url(r'^parceiros/$', parceiros, name='parceiros'),
    url(r'^projetos/$', projetos, name='projetos'),
    url(r'^doacoes/$', doacoes, name='doacoes'),
    url(r'^transparencia/$', transparencia, name='transparencia'),
    url(r'^noticias/$', noticias, name='noticias')
]