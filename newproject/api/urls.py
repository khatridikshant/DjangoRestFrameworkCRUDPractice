from django.urls import path
from .views import get_fakeuser, create_user

urlpatterns = [
    path('users/', get_fakeuser, name='get_fakeuser')
    path('users/create', create_user, name="Create User" )
]