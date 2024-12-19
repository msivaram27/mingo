import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.db import models
from srrp.models import Recipe

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)  # Track the reviewer's name
    rating = models.IntegerField()  # For rating (1-5 stars)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.recipe.name} ({self.rating} stars)'
