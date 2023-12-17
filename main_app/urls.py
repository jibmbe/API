from django.urls import path
from .views import home, create_post, signup, user_login, user_profile

urlpatterns = [
    path('', home, name='home'),
    path('accounts/profile/<str:username>/', user_profile, name='user_profile'),
    path('create_post/', create_post, name='create_post'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    # Add more paths for other views as needed
]