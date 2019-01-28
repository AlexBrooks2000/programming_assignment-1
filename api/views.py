from django.shortcuts import render
from rest_framework import generics
from books.models import Item, Shoe
from .serializers import BookSerializer

# Create your views here.
#Lists all items
class BookAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = BookSerializer
