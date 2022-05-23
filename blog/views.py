from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import PostForm

class HomeView(TemplateView):
    template_name = "main/home.html"

class BlogView(TemplateView):
    template_name = "main/blog.html"

class NewPost(CreateView):
    model = PostForm    # db
    fields = ("title", "content", "photo", "author") 
    template_name = "main/postBlog.html"
    context_object_name = "form" 
    success_url = "/post-blog"  
    def form_valid(self, form) -> bool:
  
        form.instance.user = self.request.user 
        return super(NewPost, self).form_valid(form) 