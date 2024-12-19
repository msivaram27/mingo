from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from srrp.models import Recipe

def recipe_reviews(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    reviews = recipe.reviews.all()  # Fetch related reviews
    return render(request, 'reviews/recipe_reviews.html', {'recipe': recipe, 'reviews': reviews})


def add_review(request, pk):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, pk=pk)
        content = request.POST.get('content')
        rating = request.POST.get('rating')
        Review.objects.create(recipe=recipe, content=content, rating=rating)
        return redirect('recipe_detail', pk=pk)
