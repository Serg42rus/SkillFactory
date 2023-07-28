from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cook_Book
from .serializers import Cook_BookSerializer


class Cook_BookView(APIView):
    def get(self, request):
        Cook_recepte = [
            {
                "name": Cook_recepte.name,
                "category": Cook_recepte.category,
                "text": Cook_recepte.text
            } for Cook_recepte in Cook_Book.objects.all()
        ]
        return Response(Cook_recepte)
    
    def post (self, request):
        serializer = Cook_BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response (serializer.data)
 