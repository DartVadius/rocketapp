from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blogapp.models import Post, Tag, Category, User, Contact
from django.core.paginator import Paginator
from dj.settings import ADMIN_EMAIL, APP_NAME
from blogapp.forms import ContactForm

def index(request):
    blog_posts = Post.objects.order_by('-created_at').all()[:3]
    return render(
        request,
        'blog_index.html',
        context={
            'posts': blog_posts,
            'Title': APP_NAME,
        },
    )


def subcategory(request):
    parent_id = request.GET.get('parent_id', None)
    blog_categories = Category.objects.filter(parent_id=parent_id).all()
    data = render(request, 'sub_cat.html', context={'sub_cats': blog_categories})
    return HttpResponse(data)


def post(request, post_slug):
    # blog_post = Post.objects.filter(slug=post_slug).first()
    blog_post = get_object_or_404(Post, slug=post_slug)
    return render(
        request,
        'blog_page.html',
        context={
            'post': blog_post,
            'Title': APP_NAME + ' | ' + blog_post.meta_title,
            'description': blog_post.meta_description,
            'keywords': blog_post.meta_keywords
        },
    )


def tag(request, tag_slug):
    # blog_tag = Tag.objects.filter(name=tag_slug).first()
    blog_tag = get_object_or_404(Tag, name=tag_slug)
    posts_list = Post.objects.order_by('-created_at').filter(tag=blog_tag).all()
    paginator = Paginator(posts_list, 15)
    page = request.GET.get('page')
    blog_posts = paginator.get_page(page)
    return render(
        request,
        'blog_posts.html',
        context={
            'posts': blog_posts,
            'Title': APP_NAME + ' | ' + blog_tag.name,
            'description': blog_tag.name,
            'keywords': blog_tag.name
        },
    )


def posts(request):
    posts_list = Post.objects.order_by('-created_at').all()
    paginator = Paginator(posts_list, 15)
    page = request.GET.get('page')
    blog_posts = paginator.get_page(page)
    return render(
        request,
        'blog_posts.html',
        context={
            'posts': blog_posts,
            'Title': APP_NAME + ' | Все посты',
            'description': 'всякая всячина и программирование',
            'keywords':  'php, python, django, yii2, laravel, flask'
        },
    )


def category(request, category_slug):
    # blog_category = Category.objects.filter(slug=category_slug).first()
    blog_category = get_object_or_404(Category, slug=category_slug)
    posts_list = Post.objects.order_by('-created_at').filter(category=blog_category).all()
    paginator = Paginator(posts_list, 15)
    page = request.GET.get('page')
    blog_posts = paginator.get_page(page)
    return render(
        request,
        'blog_posts.html',
        context={
            'posts': blog_posts,
            'Title': APP_NAME + ' | ' + blog_category.meta_title,
            'description': blog_category.meta_description,
            'keywords': blog_category.meta_keywords,
        },
    )


def contact(request):
    form = ContactForm()
    return render(
        request,
        'blog_contact.html',
        context={
            'form': form,
            'Title': APP_NAME + ' | contacts',
            'description': '',
            'keywords': '',
        },
    )


def send_mail(request):
    if request.is_ajax():
        model = Contact()
        model.model_populate(request)
        model.save()
        return HttpResponse(True)
    return HttpResponse(False)
