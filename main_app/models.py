
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional profile information

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Add other fields as needed

    def __str__(self):
        return self.user.username 

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', default='default_image.jpg')
    caption = models.TextField(default='Default Caption')  # Make sure this line is correctly defined
    created_at = models.DateTimeField(auto_now_add=True)

