from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse
from books.models import Book
#from . import views

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

class BookTests(TestCase):

    def setUp(self):
        Book.objects.create(item="test item", price="100", description="This is a description", image="image link", proID="0000" )

    def test_item_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.item}'
        self.assertEquals(expected_object_name, "test item")

    def test_book_list_view():
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test item")
        self.assertTemplateUsed(response, 'books/book_list.html')
