from django.contrib import admin
from .models import Recipe
from reviews.models import Review  # Import the Review model

admin.site.register(Recipe)
admin.site.register(Review)
