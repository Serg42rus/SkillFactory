from rest_framework import serializers
from .models import Cook_Book, Category

class Cook_BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cook_Book
        fields = ('id', 'name', 'category', 'text')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title',)        