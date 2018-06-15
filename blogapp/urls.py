from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='blog_index'),
    path('posts/', views.posts, name='blog_posts'),
    path('category/<str:category_slug>', views.category, name='blog_category'),
    path('post/<str:post_slug>', views.post,  name='blog_post'),
    path('tag/<str:tag_slug>', views.tag, name='blog_tag'),
    path('subcategory/', views.subcategory, name='blog_subcategory'),
    path('contact/', views.contact, name='blog_contact'),
    path('send-mail/', views.send_mail, name='send_mail'),
]

