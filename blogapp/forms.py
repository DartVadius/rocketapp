# from django.forms import ModelForm
from django import forms

from blogapp.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['created_at']
        widgets = {
            "name": forms.TextInput(
                attrs={'type': 'text', 'name': 'name', 'id': 'name', 'class': 'iform-poshytip'}),
            "email": forms.TextInput(
                attrs={'type': 'text', 'name': 'email', 'id': 'email', 'class': 'form-poshytip'}),
            "message": forms.Textarea(
                attrs={'type': 'text', 'name': 'comments', 'id': 'comments', 'class': 'form-poshytip', 'rows': "5",
                       'cols': "20"}),
        }
