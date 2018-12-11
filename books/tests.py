from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse
from .models import Book
from . import views

# Create your tests here.
class BookListTests(TestCase):

    def test_book_list_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>All books</h1>')

    def test_book_list_does_no_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'I should not be on the page')
