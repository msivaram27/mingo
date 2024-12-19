from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm, RecipeForm
from .models import Recipe
from reviews.models import Review  # Import the Review model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.csrf import csrf_protect


# User Registration
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

# Main application view (restricted to logged-in users)
@login_required
def app(request):
    return render(request, 'app.html')

# Homepage
def home(request):
    return render(request, 'home.html')

# About page
def about(request):
    return render(request, 'about.html')

# Contact page
def contact(request):
    return render(request, 'contact.html')

# Base layout view
def base(request):
    return render(request, 'base.html')

# Recipe List
def recipe_list(request):
    query = request.GET.get('q', '')  # Handle search functionality
    if query:
        recipes = Recipe.objects.filter(name__icontains(query))  # Search recipes by name
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes, 'query': query})

# Recipe Detail View
@csrf_exempt  # Use this for testing; remove in production for security
@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    reviews = Review.objects.filter(recipe=recipe)

    if request.method == 'POST':
        content = request.POST.get('content')
        rating = request.POST.get('rating')

        if content and rating:
            try:
                review = Review.objects.create(
                    recipe=recipe,
                    content=content,
                    rating=int(rating)
                )
                review.save()
                return redirect('recipe_detail', recipe_id=recipe.id)  # Redirect after successful submission
            except Exception as e:
                print(f"Error creating review: {e}")  # Log the error for debugging

    return render(request, 'recipe_detail.html', {'recipe': recipe, 'reviews': reviews})

# Add Recipe View
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)  # Handle recipe form submission
        if form.is_valid():
            form.save()  # Save the new recipe
            return redirect('home')  # Redirect to home after recipe is added
    else:
        form = RecipeForm()
    return render(request, 'form.html', {'form': form})

# Rate Recipe
def rate_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)  # Get the recipe by ID
        new_rating = int(request.POST.get('rating', 0))  # Get rating from the POST request

        if 1 <= new_rating <= 5:  # Ensure the rating is between 1 and 5
            recipe.add_rating(new_rating)  # Add rating to the recipe model
            return JsonResponse({'success': True, 'new_rating': recipe.rating})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid rating value'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

@login_required
def review_list(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    reviews = Review.objects.filter(recipe=recipe)

    return render(request, 'review_list.html', {'recipe': recipe, 'reviews': reviews})

