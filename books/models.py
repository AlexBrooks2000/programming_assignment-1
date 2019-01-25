from django.db import models

# Create your models here.
#model for item
class Book(models.Model):
    item = models.CharField(max_length=250, default="item")
    price = models.CharField(max_length=250, default="price")
    description = models.CharField(max_length=250, default="description")
    image = models.CharField(max_length=250, default="image")
    product_ID = models.CharField(max_length=4, default="0000")

    def VAT(self, price):
        int_price = int(price)
        vat = int_price*0.15
        return vat

class Shoe(Book):
    shoe_size = models.CharField(max_length=2, default="00")

    def VAT(self, price):
        int_price = int(price)
        vat = int_price*0.20
        return vat

def __string__(self):
    return self.item
