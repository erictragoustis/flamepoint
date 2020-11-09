from django.views.generic import DetailView,ListView
from .models import Portfolio, Category
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    ordering = ['-created']
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(PortfolioListView, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'Portfolio'
        context["portfolio_categories"] = Category.objects.all()
        return context

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'