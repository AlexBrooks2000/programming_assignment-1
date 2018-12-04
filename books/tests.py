from django.test import TestCase
from .models import Book

# Create your tests here.
class TestBasic2(unittest.TestCase):

    def setUp(self):
        self.a = 1

    def tearDown(self):
        del self.a

    def test_basic1(self):
        "Basic with setup"

        self.assertNotEqual(self.a, 2)

    def test_basic2(self):
        "Basic2 with setup"
        assert self.a != 2

    def test_fail(self):
        "This test should fail"
        assert self.a == 2
    # @classmethod
    # def setUpTestData(cls):
    #     Book.objects.create(item = "Test item", price = "10", description = "test description", image = "image link", ID="9999")
    #
    # def test_Item(self):
    #     book = Book.objects.get(id=1)
    #     field_label = book._meta.get_field('item').verbose_name
    #     self.assertEquals(field_label, 'item')
    #
    # def test_Price(self):
    #     book = Book.objects.get(id=1)
    #     field_label = book._meta.get_field('price').verbose_name
    #     self.assertEquals(field_label, 'price')
    #
    # def test_Description(self):
    #     book = Book.objects.get(id=1)
    #     field_label = book._meta.get_field('description').verbose_name
    #     self.assertEquals(field_label, "description")
    #
    # def test_Image(self):
    #     book = Book.objects.get(id=1)
    #     field_label = book._meta.get_field("image").verbose_name
    #     self.assertEquals(field_label, "image")
    #
    # def test_ID(self):
    #     book = Book.objects.get(id=1)
    #     field_label = book._meta.get_field("ID").verbose_name
    #     self.assertEquals(field_label, "ID")
    #
