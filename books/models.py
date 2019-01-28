from django.db import models

# Create your models here.
#model for item, example of encapulation


class Book(models.Model):

    item = models.CharField(max_length=250, default="item")
    price = models.FloatField(null=True, blank=True, default=0)
    description = models.CharField(max_length=250, default="description")
    image = models.CharField(max_length=250, default="image")
    product_ID = models.CharField(max_length=4, default="0000")
    
    def save(self, *args, **kwargs):
        vat = self.price * 0.15
        super(Book, self).save(*args, **kwargs)
        return vat
    vat = models.FloatField(editable=False)


class Shoe(Book): #Subclass of Book, example of inheritence
    shoe_size = models.CharField(max_length=2, default="00")

    def save(self, *args, **kwargs):
        vat = self.price * 0.2
        super(Book, self).save(*args, **kwargs)
        return vat


def __string__(self):
    return self.item
