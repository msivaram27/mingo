from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from .views import review_list

urlpatterns = [
    path('', views.base, name='base'),                  # Root URL maps to base view
    path('login/', views.login_view, name='login'),     # /login/ URL maps to login view
    path('app/', views.app, name='app'),                 # /app/ URL maps to app view
    path('registration/', views.registration, name='registration'),
    path('home/', views.home, name='home'),              # Home page
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('rate-recipe/<int:recipe_id>/', views.rate_recipe, name='rate_recipe'),
    path('logout/', LogoutView.as_view(next_page='base', http_method_names=['get', 'post']), name='logout'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:recipe_id>/reviews/', review_list, name='review_list'),
]
