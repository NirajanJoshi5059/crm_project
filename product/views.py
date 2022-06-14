from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from product.models import Order, Product
from customer.models import Customer
from product.forms import OrderForm
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='user:login')
def productList(request):
    products= Product.objects.all()
    context={'products':products}
    
    return render(request, 'product.html', context)
@login_required(login_url='user:login')
def createOrder(request,id):
    OrderFormSet=inlineformset_factory(Customer, Order, fields=('product','status'), extra=5)
    customer=Customer.objects.get(id=id)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form=OrderForm(request.POST or None, initial={'customer':customer})
    if request.POST:
        formset=OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('user:dashboard'))
    context={'formset':formset,'customer':customer}
    return render(request, 'create_order.html', context)

@login_required(login_url='user:login')
def updateOrder(request, id):
    order=get_object_or_404(Order, id=id)
    formset=OrderForm(instance=order)
    if request.method=='POST':
        formset=OrderForm(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('user:dashboard'))
    context={'formset':formset}
    return render(request, 'create_order.html', context)

@login_required(login_url='user:login')
def deleteOrder(request, id):
    order=get_object_or_404(Order, id=id)
    if request.POST:
        order.delete()
        return HttpResponseRedirect(reverse('user:dashboard'))
    context={'item':order}
    return render(request, 'delete.html', context)


def search(request):
    return (1)
