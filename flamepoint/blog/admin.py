from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)


def save_model(self, request, obj, form, change):
    obj.author = request.user
    super().save_model(request, obj, form, change)
