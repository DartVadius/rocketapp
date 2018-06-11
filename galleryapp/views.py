from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse("Hello from gallery")


def delete_photo(request, photo_id):
    print(photo_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))