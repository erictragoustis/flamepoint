"""flamepoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from pages.views import ajax_posting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('pages.urls', 'pages'), namespace='pages')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('portfolio/', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),
    path('ajax-posting/', ajax_posting, name='ajax_posting'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
