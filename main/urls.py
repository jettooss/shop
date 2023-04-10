from django.urls import path, re_path
from django.conf import  settings
from .views import *
from django.conf.urls.static import  static
urlpatterns = [
    path('', main, name='main'),
    path('create', create, name='create'),
    # path('/post/<str:post_id>/', show_post, name='show_post'),
    path('<slug:post_slug>/', show_post, name='show_post'),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
