from django.shortcuts import render
from customer.models import Customer
from product.models import Order
# Create your views here.
def customer_list(request, pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customer':customer,
    'orders':orders,
    'orders_count':order_count,
    'title':'Customer'}
    return render(request, 'customers.html', context)

