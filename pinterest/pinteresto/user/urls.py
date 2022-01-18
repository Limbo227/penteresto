from django.urls import path
from .views import *

urlpatterns = [
    path('author/', author, name='author'),
]