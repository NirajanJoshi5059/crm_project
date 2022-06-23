from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from customer.models import Customer
from product.models import Order
from customer.forms import CustomerForm
from customer.filters import OrderFilter
from django.contrib.auth.decorators import login_required
from user.decorators import allowed_users
# Create your views here.
@login_required(login_url='user:login')
def customer_list(request, pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    order_count=orders.count()

    myFilter=OrderFilter(request.GET, queryset=orders)
    orders=myFilter.qs

    context={'customer':customer,
    'orders':orders,
    'orders_count':order_count,
    'myFilter':myFilter,
    'title':'Customer'}
    return render(request, 'customers.html', context)

def updateCustomer(request, id):
    customer=get_object_or_404(Customer, id=id)
    # form=CustomerForm(request.POST or None, instance=customer)
    # if request.POST:
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('user:dashboard'))
    context={"customer":customer}
    return render(request,'customers.html', context)

def deleteCustomer(request,id):
    return render(request, 'customers.html')


@login_required(login_url='user:login')
@allowed_users(allowed_roles=['customer'])
def accountsetting(request):
    user=request.user.customer
    form=CustomerForm(request.POST or None, request.FILES or None, instance=user)
    if request.POST:
        if form.is_valid:
            form.save
    context={'form':form}
    return render(request,'account_setting.html', context)