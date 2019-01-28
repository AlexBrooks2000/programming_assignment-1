from django.db import models

# Create your models here.
#model for item, example of encapulation
class Item(models.Model):
    item = models.CharField(max_length=250, default="item")
    price = models.CharField(max_length=250, default="price")
    description = models.CharField(max_length=250, default="description")
    image = models.CharField(max_length=250, default="image")
    product_ID = models.CharField(max_length=4, default="0000")

<<<<<<< HEAD
    def VAT(): #Function works out VAT of item
=======
    def VAT(self, price):
>>>>>>> 10372e1a2d4dc96893baeb63ebc8c5c0ef62b61d
        int_price = int(price)
        vat = int_price*0.15
        return vat

<<<<<<< HEAD
    def __init__(self, vat):
        self.vat = VAT()

class Shoe(Item): #Subclass of Book, example of inheritence
    shoe_size = models.CharField(max_length=2, default="00")

    def VAT(): #calculates VAT but will give a different answer to book, example of polymorphism
=======
class Shoe(Book):
    shoe_size = models.CharField(max_length=2, default="00")

    def VAT(self, price):
>>>>>>> 10372e1a2d4dc96893baeb63ebc8c5c0ef62b61d
        int_price = int(price)
        vat = int_price*0.20
        return vat

<<<<<<< HEAD
    def __init__(self, vat):
        self.vat = VAT()





=======
>>>>>>> 10372e1a2d4dc96893baeb63ebc8c5c0ef62b61d
def __string__(self):
    return self.item
