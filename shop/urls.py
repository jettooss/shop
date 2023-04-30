from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authorization import views as user_views
extra_patterns = [
    path('login/', user_views.login, name='login'),
    path('register/', user_views.register, name='register'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    path('authorization/', include(extra_patterns)),

    path('__debug__/', include('debug_toolbar.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)