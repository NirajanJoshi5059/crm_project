from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from product.models import Order, Product
from customer.models import Customer
from product.forms import OrderForm
from django.forms import inlineformset_factory
# Create your views here.

def productList(request):
    products= Product.objects.all()
    context={'products':products}
    
    return render(request, 'product.html', context)

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


def updateOrder(request, id):
    order=get_object_or_404(Order, id=id)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:dashboard'))
    context={'form':form}
    return render(request, 'create_order.html', context)

def deleteOrder(request, id):
    order=get_object_or_404(Order, id=id)
    if request.POST:
        order.delete()
        return HttpResponseRedirect(reverse('user:dashboard'))
    context={'item':order}
    return render(request, 'delete.html', context)