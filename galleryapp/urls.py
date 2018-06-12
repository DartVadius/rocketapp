from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='gallery_index'),
    path('photo/<str:photo_id>', views.delete_photo, name='delete_photo'),
]