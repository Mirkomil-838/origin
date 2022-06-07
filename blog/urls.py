from django.conf import settings
from django.conf.urls.static import static

from .views import *
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('foto', foto, name='foto'),
    path('blog', Get_Product, name='blog'),
    path('video', video, name='video'),
    path('word', word, name='word'),
    path('about', about, name='about'),
    path('ADOUT', ADOUT, name='ADOUT'),
    path('contact', contact, name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
