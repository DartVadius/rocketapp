from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='gallery_index'),
    path('page/<str:gallery_slug>', views.gallery, name='gallery_page'),
    path('tag/<str:gallery_tag>', views.tag, name='gallery_tag'),
    path('photo/<str:photo_id>/delete', views.delete_photo, name='delete_photo'),
]