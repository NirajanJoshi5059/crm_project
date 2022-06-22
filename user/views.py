from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from customer.models import Customer
from product.models import Order
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from user.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.decorators import unauthenticated, admin_only, allowed_users
from django.contrib.auth.models import Group
# Create your views here.
# @allowed_users(allowed_roles=['admin'])
@login_required(login_url='user:login')
# @admin_only
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
            if user.is_superuser:
                return HttpResponseRedirect(reverse('user:dashboard'))
            else:
                return HttpResponseRedirect(reverse('user:user_view'))
        else:
            messages.info(request, 'Username or Password is Incorrect')
    context={'form':form}
    return render(request, 'login.html', context)


@unauthenticated
def register_view(request):
    form=CreateUserForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user)
            messages.success(request, "Account has been created for "+username)
            return HttpResponseRedirect(reverse('user:login'))
    context={'form':form}
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))

@login_required(login_url='user:login')
@allowed_users(allowed_roles=['customer'])
def user_view(request):
    orders=request.user.customer.order_set.all()
    total_order=orders.count()
    delivered=orders.filter(status='Delivery').count()
    pending=orders.filter(status='Pending').count()

    print("Orders", orders)
    context={"orders":orders,
    'total_order':total_order,
    'delivered':delivered,
    'pending':pending,
    }
    return render(request,'user.html', context)