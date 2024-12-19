from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Recipe

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'image', 'ingredients', 'instructions', 'video_url', 'prep_time']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'background-color: #f0f8ff; color: #333; border-color: #007bff;',
                'placeholder': 'Recipe Name'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'style': 'background-color: #f9f9f9; color: #333;'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'background-color: #e6ffe6; color: #333; border-color: #28a745;',
                'placeholder': 'List the ingredients'
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'background-color: #ffffe6; color: #333; border-color: #ffc107;',
                'placeholder': 'Enter the instructions'
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'style': 'background-color: #f0f8ff; color: #333; border-color: #007bff;',
                'placeholder': 'Video URL'
            }),
            'prep_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'background-color: #e6f0ff; color: #333; border-color: #17a2b8;',
                'placeholder': 'Preparation Time in Minutes'
            }),
        }
