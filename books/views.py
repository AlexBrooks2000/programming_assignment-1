from django.shortcuts import render
from django.views.generic import ListView
from books.models import Book, Shoe

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

class ShoeListView(ListView):
    model = Shoe
    template_name = 'book_list.html'
