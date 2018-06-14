# from django.forms import ModelForm
from django import forms

from galleryapp.models import Gallery, Photo


class GalleryForm(forms.ModelForm):
    files = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False, label='Photos')

    class Meta:
        model = Gallery
        # fields = '__all__'
        exclude = ['created_at']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['path']

