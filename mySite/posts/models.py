from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100)
    img  = models.ImageField(default='default.jpg', blank=True)
