from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import OrderForm, SignUpForm, CustomerForm
from . filters import OrderFilter
# Create your views here.
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from . decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib import messages

@unauthenticated_user
def signupuser(request):
    form = SignUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, 'Account created successfully for '+ username)
            return redirect('loginuser')
        else:
            context = {
                'form': form,
                'error': form.errors
            }
            return render(request, 'accounts/signupuser.html', context )
    else:
        return render(request, 'accounts/signupuser.html', {'form': form})

@unauthenticated_user
def loginuser(request):
    if request.method == 'GET':
        context = {
            'form':AuthenticationForm()
        }
        return render(request, 'accounts/loginuser.html', context )
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'error': 'username and password doest not match'
            }
            return render(request, 'accounts/loginuser.html', context )
        else:
            login(request,user)
            return redirect('home')


@login_required(login_url="loginuser")
@admin_only
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()
    context = {
        'orders':orders,
        'customers':customers,
        'total_customers':total_customers,
        'delivered':delivered,
        'pending':pending,
        'total_orders':total_orders,
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url="loginuser")
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html',{'products':products})



@login_required(login_url="loginuser")
@allowed_users(allowed_roles=['customer'])
def userProfile(request):
    orders = request.user.customer.order_set.all()
    print('orders:',orders)
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()
    context = {
        'orders':orders,
        'delivered':delivered,
        'pending':pending,
        'total_orders':total_orders
    }
    return render(request,'accounts/user.html', context)


@login_required(login_url="loginuser")
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {
        'form':form,
    }
    return render(request, 'accounts/account_settings.html',context)


@login_required(login_url="loginuser")
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'customer':customer,
        'orders':orders,
        'total_orders':total_orders,
        'myFilter':myFilter
    }
    return render(request, 'accounts/customer.html',context)


@login_required(login_url="loginuser")
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'accounts/order_form.html',context) 


@login_required(login_url="loginuser")
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url="loginuser")
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    context={
        'order':order
    }
    return render(request, 'accounts/delete.html',context)


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('loginuser')