from django.views.generic import DetailView
from .models import Portfolio
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'