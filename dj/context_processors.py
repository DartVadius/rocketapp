from blogapp.models import Category, Post
import re


def add_categories_to_context(request):
    categories = Category.objects.filter(parent_id=None).order_by('name').all()
    posts = Post.objects.order_by('-created_at').all()[:3]
    images = dict()
    for post in posts:
        if re.search('(<img .* />)', post.short_text):
            images[post.id] = re.search('(<img .* />)', post.short_text).group(1)
        else:
            images[post.id] = '<img alt="" src="/static/img/dummies/t1.jpg" />'
    return {
        'categories': categories,
        'posts': posts,
        'images': images,
    }
