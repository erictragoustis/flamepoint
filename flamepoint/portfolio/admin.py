from django.contrib import admin
from .models import Category,Tag,Portfolio, Technology

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Portfolio)
admin.site.register(Technology)