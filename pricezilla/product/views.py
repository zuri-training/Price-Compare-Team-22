from unicodedata import category
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Category

def furniture(request):
    category = Category.objects.filter(name='Furnitures')
    product_list = Product.objects.filter(category=category[0])
    paginator = Paginator(product_list, 30) # Show 30 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    loop = range(3)
    return render(request, 'product/furnitures.html', {'page_obj': page_obj, 'loop': loop})
