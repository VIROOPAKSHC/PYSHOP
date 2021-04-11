from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)


class Offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()


class Help(models.Model):
    Subject=models.CharField(max_length=255)
    Description=models.CharField(max_length=2000)


class Home(models.Model):
    name=models.CharField(max_length=10)
    Description=models.CharField(max_length=255)