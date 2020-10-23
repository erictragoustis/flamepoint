
from django.urls import path
from .views import  BlogDetailView

urlpatterns = [
path(route='<slug:slug>/', view=BlogDetailView.as_view(), name='postDetail'),
]