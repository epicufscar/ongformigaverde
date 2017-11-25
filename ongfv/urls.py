from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('ong.urls')),
    url(r'^admin/', admin.site.urls),
]
