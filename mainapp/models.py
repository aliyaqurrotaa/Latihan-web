from django.db import models

# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=100)
    descrption = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=PROTECT)


class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=CASCADE)
