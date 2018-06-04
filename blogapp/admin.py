from django.contrib import admin
from .models import Post, Profile, Tag, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'category', 'display_tags')
    list_filter = ('category', 'created_at', 'tag')

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'short_text', 'text', 'category', 'tag')
        }),
        ('Meta data', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'parent_id')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)

