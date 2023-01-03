from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=200, unique=True)
    img_url = models.URLField()
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    blog = models.ForeignKey(BlogPost, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.body