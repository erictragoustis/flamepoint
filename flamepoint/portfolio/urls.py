
from django.urls import path
from .views import  PortfolioDetailView

urlpatterns = [
path(route='<slug:slug>/', view=PortfolioDetailView.as_view(), name='portfolioDetail'),
]