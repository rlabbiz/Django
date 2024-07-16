from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.allPosts, name='post'),
    path('<slug:slug>', views.postDetail, name='post_detail'),
]