from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('foo/', views.foo, name='foo'),
    path('post/<str:post_slug>', views.post, name='blog_post'),
]
