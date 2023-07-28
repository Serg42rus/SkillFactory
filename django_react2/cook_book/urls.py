from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('api/cook_book/', views.Cook_BookView.as_view() ),
]