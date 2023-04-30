from django.urls import path, re_path
from django.conf import  settings
from .views import *
from django.conf.urls.static import  static
urlpatterns = [
    path('', main, name='main'),
    path('create', create, name='create'),
    path('cabinet', cabinet, name='cabinet'),
    path('logout/', logoutUser, name='logout'),
    path('checkout', checkout, name='checkout'),

    path('orders/<int:order_id>/delete/', delete_order, name='delete_order'),

    # path('/post/<str:post_id>/', show_post, name='show_post'),
    path('<slug:post_slug>/', show_post, name='show_post'),

]
