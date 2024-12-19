from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes/')
    ingredients = models.TextField()
    instructions = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    prep_time = models.IntegerField()
    rating = models.FloatField(default=0.0)  # Stores the average rating
    rating_count = models.IntegerField(default=0)  # Counts the number of ratings
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def add_rating(self, new_rating):
        # Calculate new average rating
        total_rating = self.rating * self.rating_count + new_rating
        self.rating_count += 1
        self.rating = total_rating / self.rating_count
        self.save()
