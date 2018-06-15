from galleryapp.models import Photo, Gallery, Tag
from django.core.paginator import Paginator
from rest_framework import viewsets
from galleryapp.serializers import GallerySerializer, PhotoSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-created_at')
    serializer_class = GallerySerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-created_at')
    serializer_class = PhotoSerializer
