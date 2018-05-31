from django.contrib import admin

from .models import Post, Profile, Tag, Category

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Post)

