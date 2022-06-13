from django.http import HttpResponseRedirect
from django.shortcuts import render
from customer.models import Customer
from product.models import Order
# Create your views here.

def dashboard(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total_order=Order.objects.all().count()
    delivered=orders.filter(status='Delivery').count()
    pending=orders.filter(status='Pending').count()

    context={'customers':customers, 'orders':orders,
    'total_order':total_order,
    'delivered':delivered,
    'pending':pending
    }
    return render(request,'dashboard.html', context)