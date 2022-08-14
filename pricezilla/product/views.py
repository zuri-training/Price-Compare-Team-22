from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category

def category(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    product_list = Product.objects.filter(category=category).order_by('?')
    paginator = Paginator(product_list, 30) # Show 30 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'furniture.html', {'page_obj': page_obj, 'category': category})

def detail (request, c_slug=None, p_slug=None):
    product = get_object_or_404(Product, slug=p_slug)

    return render(request, 'description.html', {'product': product})