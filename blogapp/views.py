from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blogapp.models import Post, Tag, Category, Profile
from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import re


def index(request):
    blog_posts = Post.objects.order_by('-created_at').all()[:3]
    images = dict()
    for blog_post in blog_posts:
        if re.search('(<img .* />)', blog_post.short_text):
            images[blog_post.id] = re.search('(<img .* />)', blog_post.short_text).group(1)
        else:
            images[blog_post.id] = '<img alt="" src="/static/img/dummies/t1.jpg" />'
    return render(
        request,
        'blog_index.html',
        context={'posts': blog_posts, 'images': images},
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


def posts(request):
    posts_list = Post.objects.order_by('-created_at').all()
    paginator = Paginator(posts_list, 15)
    page = request.GET.get('page')
    blog_posts = paginator.get_page(page)
    return render(
        request,
        'blog_posts.html',
        context={'posts': blog_posts, 'Title': 'Все посты'},
    )


def category(request, category_slug):
    return HttpResponse(category_slug)
