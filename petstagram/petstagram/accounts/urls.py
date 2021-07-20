from django.urls import path, include
from petstagram.accounts.views import signin, signup, signout, user_profile

urlpatterns = [
    path('profile/<int:pk>', user_profile, name='profile details'),
    path('signup/', signup, name='sign up user'),
    path('signin/', signin, name='sign in user'),
    path('signout/', signout, name='sign out user'),
]