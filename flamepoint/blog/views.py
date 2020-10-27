
from django.views.generic import DetailView,ListView
from .models import Post, Category
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
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

class BlogListView(ListView):
    paginate_by = 10
    model = Post
    template_name = 'blog/blog_list.html'
    ordering = ['-created']
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'Blog Posts List'
        context["categories"] = Category.objects.values('title','slug').annotate(dcount=Count('post'))
        return context

class PostByCategoryListView(ListView):
    
    template_name = 'blog/blog_list.html'


    #Queryset from https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects
    def get_queryset(self):
        self.Category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.Category)
    
    def get_context_data(self, *args, **kwargs):
        data = super(PostByCategoryListView, self).get_context_data(*args, **kwargs)
        data['page_title'] = 'Posts of Category: ' + str(self.Category)
        data['the_category'] = str(self.Category)
        data["categories"] = Category.objects.values('title','slug').annotate(dcount=Count('post'))
        
        return data