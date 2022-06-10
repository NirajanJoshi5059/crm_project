from this import d
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')