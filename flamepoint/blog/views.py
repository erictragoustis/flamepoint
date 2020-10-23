
from django.views.generic import DetailView
from .models import Post, Category
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'