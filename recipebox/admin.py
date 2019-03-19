from django.contrib import admin
from .models import Author, Unit, Recipe  # Food

admin.site.register(Recipe)
admin.site.register(Author)
admin.site.register(Unit)
# admin.site.register(Food)
