from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.CharField(max_length=255, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_id = models.ForeignKey('self', default=None, null=True, on_delete=models.SET(None), blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(null=False, max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Post (models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = models.CharField(max_length=255, unique=True, blank=False)
    short_text = models.TextField(max_length=255, blank=True)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=45, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET(None), null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

#
# class Comment(models.Model):
#     text = models.TextField(null=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     post = models.OneToOneField(Post, on_delete=models.CASCADE)
#     parent_id = models.ForeignKey('self', default=None, null=True)


