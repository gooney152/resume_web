from typing import Text
from django import forms
from django.forms.widgets import TextInput, Widget
from .models import ContactProfile

class ContactForm(forms.ModelForm):
    #rendered on the front end
    name = forms.CharField(max_length=75, required=True,
            widget= forms.TextInput(attrs={
                'placeholder': '*Full name',
                'class': 'form-control'
            }))

    email = forms.EmailField(max_length=300, required=True,
            widget=forms.TextInput(attrs={
                'placeholder': '*Email',
                'class': 'form-control'
            }))

    message = forms.CharField(max_length=1000, required=True,
            widget=forms.Textarea(attrs={
                'placeholder': '*Enter message',
                'rows': 6,
            }))

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message',)
    