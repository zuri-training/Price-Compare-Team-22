from django.contrib import admin
from .models import Product, Store, Category, Comment

admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Comment)

# Register your models here.
