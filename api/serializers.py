from rest_framework import serializers
from books.models import Book, Shoe

#Creates a new field of text
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('item', 'price', 'description', 'image', 'product_ID')
