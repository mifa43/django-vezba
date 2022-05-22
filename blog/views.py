from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "main/home.html"

class BlogView(TemplateView):
    template_name = "main/blog.html"

class NewPost(CreateView):
    pass