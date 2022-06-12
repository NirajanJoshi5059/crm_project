
from django.http import HttpResponseRedirect
from django.shortcuts import render
from product.models import Product
# Create your views here.

def productList(requsest):
    products= Product.objects.all()
    context={'products':products}
    
    return render(requsest, 'product.html', context)
