"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import I
from django.contrib import admin
from django.urls import path
from blog.views import HomeView, BlogView, NewPost
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from auth.views import Register as vs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name="home"),
    path('blog/', BlogView.as_view(), name="blog"),
    path("post-blog/", NewPost.as_view(), name="post-blog" ),
    path("register/", vs.as_view(), name="register" ),


]
urlpatterns += staticfiles_urlpatterns()