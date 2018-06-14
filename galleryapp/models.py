import time
import os
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Count
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from blogapp.models import Tag


class Gallery(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    meta_title = models.CharField(max_length=45, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
            if not self.slug_is_unique():
                self.slug = self.slug + '_' + str(int(time.time()))

        super(Gallery, self).save(*args, **kwargs)

    def slug_is_unique(self):
        count = Gallery.objects.filter(slug=self.slug).count()
        if count > 0:
            return False
        return True

    def get_random_image(self):
        """Return random image"""
        return self.photo_set.order_by('?').first()

    def get_related_galleries(self, num=3):
        """
        Return list of gallery objects with same tags in random order
        num is a quantity of receiving rows
        """
        return Gallery.objects.filter(~models.Q(id=self.id), tag__in=self.tag.all()).order_by('?').all()[:num]

    def __str__(self):
        return self.name


class Photo(models.Model):
    path = models.CharField(max_length=255, unique=False, blank=False)
    title = models.CharField(max_length=255, unique=False, blank=True)
    alt = models.CharField(max_length=255, unique=False, blank=True)
    description = RichTextField(blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=False)

    def __str__(self):
        if self.title:
            return self.title
        return 'photo'

    def delete(self, using=None, keep_parents=False):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = base + self.path
        if os.path.isfile(path):
            os.remove(path)
        thumb_path = self.get_thumb()
        path = base + thumb_path
        if os.path.isfile(path):
            os.remove(path)
        super(Photo, self).delete(using, keep_parents)

    def get_thumb(self):
        """Return thumbnail path"""
        splited = self.path.split('/')
        splited[-1] = 'thumb_' + splited[-1]
        thumb_path = '/'.join(splited)
        return thumb_path

    def display_img(self):
        return mark_safe('<img src="%s" height="120px" />' % self.get_thumb())

    display_img.short_description = 'Image'
