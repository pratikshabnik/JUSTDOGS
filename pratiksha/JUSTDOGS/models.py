from django.db import models

class Justdogs(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    imgPath = models.CharField(max_length=100)

class Order(models.Model):
    dogname = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    number= models.BigIntegerField()


