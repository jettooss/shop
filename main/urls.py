from django.urls import path, re_path
from django.conf import  settings
from .views import *
from django.conf.urls.static import  static
urlpatterns = [
    path('', main, name='main'),
    path('/create', create, name='create'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
