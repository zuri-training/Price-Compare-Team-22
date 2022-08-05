
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms import inlineformset_factory
from .filters import OrderFilter

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .forms import OrderForm
from .serializers import ProductSerializer
from django.contrib.auth.forms import UserCreationForm



# Create your views here
def signUp(request):
    
        form = UserCreationForm()
        
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
        
        context = {'form':form}
        
    
        return render(request, 'product/sign-up.html', context)

def LogIn(request):
  
        
    context = {}
    return render(request, 'product/login.html')
def home(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products':products})

def laptop(request):
    return render(request,'product/laptops.html')

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders  = myFilter.qs
    
    
    context = {'customer':customer, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter}
    return render(request, 'product/customer.html', context)
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # 
    #form = OrderForm(initial={'customer':customer})
    
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/dashboard/')
    
    context = {'formset':formset}
    
    return render(request, 'product/order_form.html', context)
def dashboard(request):
    orders= Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()
    available = orders.filter(status='Available').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'available':available, "pending":pending}
    
    return render(request, 'product/dashboard.html', context)



def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':  
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
                form.save()
                return redirect('/dashboard/')
    context = {'form':form}
    return render(request, 'product/order_form.html', context)
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method =="POST":
        order.delete()
        return redirect('/dashboard/')
    
    context={'item':order}
    return render(request, 'product/delete.html', context)

@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'List':'/product-list/',
        'Product View':'/product-view/<str:pk>/',
        'Create': '/product-create/',
        'Update':'/product-update/<str:pk>/',
        'Delete':'/product-delete/<str:pk>/',
        
    }
    
    return Response(api_urls)

@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    
    return Response("Product successfully deleted")

