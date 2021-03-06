from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import time, re


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    meta_title = models.CharField(max_length=45, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    parent_id = models.ForeignKey('self', default=None, null=True, on_delete=models.SET(None), blank=True)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
            if not self.slug_is_unique():
                self.slug = self.slug + '_' + str(int(time.time()))

        super(Category, self).save(*args, **kwargs)

    def slug_is_unique(self):
        count = Category.objects.filter(slug=self.slug).count()
        if count > 0:
            return False
        return True

    def __str__(self):
        return self.name

    def has_children(self):
        count = Category.objects.filter(parent_id=self.id).count()
        if count > 0:
            return True
        return False
    #
    # def post_count(self):
    #     return Post.objects.filter(category=self).count()


class Tag(models.Model):
    name = models.CharField(null=False, max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post (models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    short_text = RichTextUploadingField('short description', blank=True)
    text = RichTextUploadingField('full text', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=45, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET(None), null=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def display_tags(self):
        return ', '.join([tag.name for tag in self.tag.all()])

    display_tags.short_description = 'Tags'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title)
            if not self.slug_is_unique():
                self.slug = self.slug + '_' + str(int(time.time()))

        super(Post, self).save(*args, **kwargs)

    def slug_is_unique(self):
        count = Post.objects.filter(slug=self.slug).count()
        if count > 0:
            return False
        return True

    def get_title_picture(self):
        if re.search('(<img .* />)', self.short_text):
            return re.search('(<img .* />)', self.short_text).group(1)
        else:
            return '<img alt="" src="/static/img/dummies/t1.jpg" />'

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def model_populate(self, request):
        self.name = request.POST.get('name')
        self.email = request.POST.get('email')
        self.message = request.POST.get('comment')

    def __str__(self):
        return self.name
