from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post", null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='postImage')
    author = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    
    def __str__(self):
            return self.title