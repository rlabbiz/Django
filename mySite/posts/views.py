from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

def allPosts(request):
    return render(request, 'home.html', {'posts': Posts.objects.all()})

def postDetail(request, slug):
    post = Posts.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post': post})

