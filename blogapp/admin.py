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

    class Media:
        # Put your jquery in - automatically included by django but it appears below the chosen.jquery.min.js,
        # adding it again just seems to shift it above
        js = (
              'js/jquery-3.3.1.min.js',
              'chosen/chosen.jquery.min.js',
              'chosen/chosen.proto.min.js',
              'js/chosen_admin.js')
        css = {'all': ('chosen/chosen.min.css', 'css/chosen_admin.css')}


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

