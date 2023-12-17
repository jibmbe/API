# main_app/forms.py

from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # Add additional fields if needed
    full_name = forms.CharField(max_length=100)

    class Meta:
        model = User  # Use the User model
        fields = UserCreationForm.Meta.fields + ('full_name',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']