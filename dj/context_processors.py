from blogapp.models import Category, Post, Tag


def add_categories_to_context(request):
    categories = Category.objects.filter(parent_id=None).order_by('name').all()
    categories_footer = Category.objects.order_by('name').all()
    posts = Post.objects.order_by('-created_at').all()[:5]
    tags = Tag.objects.order_by('?').all()[:10]
    return {
        'categories': categories,
        'posts_footer': posts,
        'categories_footer': categories_footer,
        'tags': tags,
    }
