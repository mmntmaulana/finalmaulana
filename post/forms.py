from django import forms
from django.forms import ModelForm
from .models import Post
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, Textarea

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        labels = {
        "is_active": "Active"
        }
        exclude = ['id']
    
      
class RegistrationModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        help_texts = {
            'username': None,
        }
        widgets = {
            'password': PasswordInput()
        }