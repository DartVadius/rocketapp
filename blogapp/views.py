from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import Post, Tag, Category, Profile


def index(request):
    posts = Post.objects.all()
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(
        request,
        'blog_index.html',
        context={'posts': posts},
    )

def foo(request):
    return HttpResponse("Foo")


def post(reqest, post_slug):
    print(post_slug)
    return HttpResponse("Post")
