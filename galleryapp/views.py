from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from galleryapp.models import Photo


def index(request):
    return HttpResponse("Hello from gallery")


@permission_required('True')
def delete_photo(request, photo_id):
    Photo.objects.get(id=photo_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))