from django.contrib import admin
from dj.service.services import Files

from .models import Gallery, Photo
from .forms import GalleryForm, PhotoForm


class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm

    # override original admin template
    # change_form_template = 'admin_change_form.html'

    list_display = ('name', 'created_at',)
    list_filter = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'files', 'tag')
        }),
        ('Meta data', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords',)
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

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # extra_context['osm_data'] = ....  add extra context here
        return super(GalleryAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if request.FILES.getlist('files'):
            Files.images_to_gallery_upload(obj, request.FILES.getlist('files'))


class PhotoAdmin(admin.ModelAdmin):

    form = PhotoForm

    list_display = ('display_img', 'title', 'gallery',)
    readonly_fields = ('display_img',)
    list_filter = ('gallery',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
