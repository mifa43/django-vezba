from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Post

class HomeView(TemplateView):
    template_name = "main/home.html"

class BlogView(ListView):
    model = Post
    context_object_name = "post"
    template_name = "main/blog.html"

class NewPost(CreateView):
    model = Post   # db
    fields = ("title", "content", "photo") 
    template_name = "main/postBlog.html"
    context_object_name = "form" 
    success_url = "/post-blog"  
    def form_valid(self, form) -> bool:
          
        form.instance.user = self.request.user 
        form.instance.author = self.request.user 

        return super(NewPost, self).form_valid(form)  