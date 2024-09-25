from django.urls import path
from .views import get_users, create_user

urlpatterns = [
    path('users/', get_users, name="Get All Users"),
    path('users/create', create_user, name="Create User" )
]