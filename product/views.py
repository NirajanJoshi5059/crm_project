from audioop import reverse
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def productList(requsest):
    return render(requsest, 'product.html')
