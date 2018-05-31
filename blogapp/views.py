from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def foo(request):
    return HttpResponse("Foo")


def post(reqest, post_slug):
    print(post_slug)
    return HttpResponse("Post")
