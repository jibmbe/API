from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

def user_profile(request, username):
    user = User.objects.get(username=username)
    user_posts = Post.objects.filter(user=user).order_by('-created_at')
    return render(request, 'user_profile.html', {'user': user, 'user_posts': user_posts})
