from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='blog_index'),
    path('categories/', views.categories, name='blog_categories'),
    path('category/<str:category_slug>', views.category, name='blog_category'),
    path('post/<str:post_slug>', views.post, name='blog_post'),
    path('tag/<str:tag_slug>', views.tag, name='blog_tag'),
    path('subcategory/', views.subcategory, name='blog_subcategory'),
]
