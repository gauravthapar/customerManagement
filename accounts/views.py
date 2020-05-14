from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import OrderForm
from . filters import OrderFilter
# Create your views here.

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

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html',{'products':products})

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

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('home')
    context={
        'order':order
    }
    return render(request, 'accounts/delete.html',context)