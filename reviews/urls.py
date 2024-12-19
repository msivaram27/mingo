from django.urls import path
from . import views

urlpatterns = [
    path('reviews/<int:recipe_id>/', views.recipe_reviews, name='recipe_reviews'),
    path('add_review/<int:pk>/', views.add_review, name='add_review'),
]
