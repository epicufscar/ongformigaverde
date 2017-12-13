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
    url(r'^noticias/$', noticias, name='noticias'),
    url(r'^noticia/(?P<id>[0-9]+)$', noticia, name='noticia'),
    url(r'^projeto/(?P<id>[0-9]+)$', projeto, name='projeto')
]
