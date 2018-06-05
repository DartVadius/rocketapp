from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blogapp.models import Post, Tag, Category, Profile
from django.core import serializers
import re


def index(request):
    posts = Post.objects.order_by('-created_at').all()[:3]
    images = dict()
    for post in posts:
        if re.search('(<img .* />)', post.short_text):
            images[post.id] = re.search('(<img .* />)', post.short_text).group(1)
        else:
            images[post.id] = '<img alt="" src="/static/img/dummies/t1.jpg" />'
    return render(
        request,
        'blog_index.html',
        context={'posts': posts, 'images': images},
    )


def subcategory(request):
    parent_id = request.GET.get('parent_id', None)
    blog_categories = Category.objects.filter(parent_id=parent_id).all()
    data = render(request, 'sub_cat.html', context={'sub_cats': blog_categories})
    return HttpResponse(data)


def post(request, post_slug):
    return HttpResponse(post_slug)


def tag(request, tag_slug):
    return HttpResponse(tag_slug)


def categories(request):
    categories = Category.objects.filter(parent_id=0).order_by('name').all()
    return HttpResponse('Categories')


def category(request, category_slug):
    return HttpResponse(category_slug)
