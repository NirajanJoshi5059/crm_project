from multiprocessing import context
from re import A
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from customer.models import Customer
from product.models import Order
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from user.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.decorators import unauthenticated, allowed_users
# Create your views here.

@login_required(login_url='user:login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total_order=Order.objects.all().count()
    delivered=orders.filter(status='Delivery').count()
    pending=orders.filter(status='Pending').count()

    context={'customers':customers, 'orders':orders,
    'total_order':total_order,
    'delivered':delivered,
    'pending':pending,
    'title':'Dashboard'
    }
    return render(request,'dashboard.html', context)


@unauthenticated
def login_view(request):
    form=AuthenticationForm(request.POST or None)
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('user:dashboard'))
        else:
            messages.info(request, 'Username or Password is Incorrect')
    context={'form':form}
    return render(request, 'login.html', context)


@unauthenticated
def register_view(request):
    form=CreateUserForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, "Account has been created for "+user)
            return HttpResponseRedirect(reverse('user:login'))
    context={'form':form}
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))

def user_view(request):
    context={}
    return render(request,'user.html', context)