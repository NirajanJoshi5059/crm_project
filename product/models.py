from customer.models import Customer
from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Electronics','ELECTRONICS'),
        ('Grossery', 'GROSSERY'),
        ('Clothings','CLOTHINGS'),
        ('HomeAppliance','HOME APPLIANCE')
    )
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tag= models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ('Pending','PENDING'),
        ('Out for delivery','OUT FOR DELIVERY'),
        ('Delivery', 'DELIVERY')
    )
    customer= models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
