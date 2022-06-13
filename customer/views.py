from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from customer.models import Customer
from product.models import Order
from customer.forms import CustomerForm
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

def updateCustomer(request, id):
    customer=get_object_or_404(Customer, id=id)
    form=CustomerForm(request.POST or None, instance=customer)
    if request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:dashboard'))
    context={"customer":customer}
    return render(request,'customers.html', context)

def deleteCustomer(request,id):
    return render(request, 'customers.html')