from django.db import models


class Ad(models.Model):
    Id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=4000)
    address = models.CharField(max_length=500)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
