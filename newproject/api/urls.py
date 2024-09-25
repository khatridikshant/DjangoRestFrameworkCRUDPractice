from django.urls import path
from .views import get_fakeuser

urlpatterns = [
    path('users/', get_fakeuser, name='get_fakeuser')
]