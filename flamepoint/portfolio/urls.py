
from django.urls import path
from .views import  PortfolioDetailView, PortfolioListView

urlpatterns = [
path('', PortfolioListView.as_view(), name='allPortfolios'),
path(route='<slug:slug>/', view=PortfolioDetailView.as_view(), name='portfolioDetail'),
]