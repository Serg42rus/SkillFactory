import django_filters.rest_framework
from django.shortcuts import render
from .models import Cook_Book, Category
from .serializers import Cook_BookSerializer, CategorySerializer
from rest_framework import viewsets

class Cook_BookViewset(viewsets.ModelViewSet):
    queryset = Cook_Book.objects.all()
    serializer_class = Cook_BookSerializer
    filter_beckends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["category"]

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    filter_beckends = [django_filters.rest_framework.DjangoFilterBackend]   
    filterset_fields = ["title"]

    
     

 