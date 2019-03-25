from django.contrib import admin
from .models import Author, Recipe

admin.site.register(Recipe)
admin.site.register(Author)
