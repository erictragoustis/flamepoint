
from django.views.generic import DetailView
from .models import Post, Category
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count


# Create your views here.

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   

        categories = Category.objects.values('title').annotate(dcount=Count('post'))
        context["categories"] = categories


        return context