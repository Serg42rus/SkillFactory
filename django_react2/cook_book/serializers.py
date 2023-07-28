from rest_framework import serializers
from .models import Cook_Book

class Cook_BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cook_Book
        fields = ('id', 'name', 'category', 'text')