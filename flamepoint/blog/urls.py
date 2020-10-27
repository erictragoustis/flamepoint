
from django.urls import path
from .views import  BlogDetailView,BlogListView,PostByCategoryListView

urlpatterns = [
path('', BlogListView.as_view(), name='allPosts'),
path(route='<slug:slug>/', view=BlogDetailView.as_view(), name='postDetail'),
path('categories/<slug:slug>/', PostByCategoryListView.as_view(), name='postListCategory'),

]