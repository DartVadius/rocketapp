from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import Post, Tag, Category
from django.core.paginator import Paginator
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
    blog_post = Post.objects.filter(slug=post_slug).first()
    return render(
        request,
        'blog_page.html',
        context={'post': blog_post, 'Title': blog_post.title},
    )


def tag(request, tag_slug):
    blog_tag = Tag.objects.filter(name=tag_slug).first()
    posts_list = Post.objects.order_by('-created_at').filter(tag=blog_tag).all()
    paginator = Paginator(posts_list, 15)
    page = request.GET.get('page')
    blog_posts = paginator.get_page(page)
    return render(
        request,
        'blog_posts.html',
        context={'posts': blog_posts, 'Title': blog_tag.name},
    )


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
    blog_category = Category.objects.filter(slug=category_slug).first()
    posts_list = Post.objects.order_by('-created_at').filter(category=blog_category).all()
    paginator = Paginator(posts_list, 15)
    page = request.GET.get('page')
    blog_posts = paginator.get_page(page)
    return render(
        request,
        'blog_posts.html',
        context={'posts': blog_posts, 'Title': blog_category.name},
    )
