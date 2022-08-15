from unicodedata import category
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def furniture(request):
        category = Category.objects.filter(name='Furnitures')
        product_list = Product.objects.filter(category=category.first())
        paginator = Paginator(product_list, 30) # Show 30 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        loop = range(3)
        return render(request, 'product/furniture.html')

@login_required(login_url='login')
def entertainement(request):
        category = Category.objects.filter(name='Furnitures')
        product_list = Product.objects.filter(category=category.first())
        paginator = Paginator(product_list, 30) # Show 30 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        loop = range(3)
        return render(request, 'product/entertainement.html')

@login_required(login_url='login')
def kitchen(request):
        category = Category.objects.filter(name='kitchen')
        product_list = Product.objects.filter(category=category.first())
        paginator = Paginator(product_list, 30) # Show 30 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        loop = range(3)
        return render(request, 'product/kitchen.html')

@login_required(login_url='login')
def laundry(request):
        category = Category.objects.filter(name='laundry')
        product_list = Product.objects.filter(category=category.first())
        paginator = Paginator(product_list, 30) # Show 30 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        loop = range(3)
        return render(request, 'product/laundry.html')