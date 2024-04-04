from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserRetrieveView.as_view(), name='login'),
]