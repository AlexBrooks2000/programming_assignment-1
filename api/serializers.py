from rest_framework import serializers
from books.models import Item, Shoe

#Creates a new field of text
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item', 'price', 'description', 'image', 'product_ID', 'VAT')
