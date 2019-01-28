from django.shortcuts import render
from django.views.generic import ListView
from books.models import Item, Shoe

# Create your views here.
class BookListView(ListView):
    model = Item
    template_name = 'book_list.html'

class ShoeListView(ListView):
    model = Shoe
    template_name = 'book_list.html'
