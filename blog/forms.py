from django import forms
from .models import Post
from django.forms import ModelForm

class PostForm(ModelForm):
    
    model = Post
    fields = ["title", "content", "created_on", "photo", "author"]

