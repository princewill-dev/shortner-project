from django.urls import path
from . import views

urlpatterns = [
    path('/', views.shorten_url, name='home'),
    path('test/', views.test_view, name='test'),
]