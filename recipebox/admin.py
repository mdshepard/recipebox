from django.contrib import admin
from .models import Author, Food, Unit, Recipe

admin.site.register(Food)
admin.site.register(Author)
admin.site.register(Unit)
admin.site.register(Recipe)
