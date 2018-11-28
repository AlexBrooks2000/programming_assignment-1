from django.db import models

# Create your models here.
class Book(models.Model):
    item = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    ID = models.CharField(max_length=10)

def __string__(self):
    return self.title
