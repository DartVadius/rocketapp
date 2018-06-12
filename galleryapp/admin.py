from django.contrib import admin
from .models import Gallery, Photo
from .forms import GalleryForm, PhotoForm
from django.core.files.storage import FileSystemStorage
import time
from PIL import Image, ImageFilter


class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm

    # change original admin template
    change_form_template = 'change_form.html'

    list_display = ('name', 'created_at',)
    list_filter = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'files',)
        }),
        ('Meta data', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords',)
        }),
    )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # extra_context['osm_data'] = ....  add extra context here
        return super(GalleryAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if request.FILES.getlist('files'):
            for file in request.FILES.getlist('files'):
                fs = FileSystemStorage()
                filename = fs.save(str(obj.id) + '/' + str(round(time.time())) + '_' + file.name, file)
                splited = filename.split('/')
                splited[-1] = 'thumb_' + splited[-1]
                thumb_path = '/'.join(splited)
                uploaded_file_url = fs.url(filename)
                img = Photo()
                img.gallery_id = obj.id
                img.path = uploaded_file_url
                img.save()
                img = Image.open('media/' + filename)
                size = (280, 280)
                img.thumbnail(size)
                img.save('media/' + thumb_path)


class PhotoAdmin(admin.ModelAdmin):

    form = PhotoForm

    list_display = ('gallery', 'display_img',)
    readonly_fields = ('display_img',)
    list_filter = ('gallery',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
