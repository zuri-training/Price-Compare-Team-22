from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Tag)

# Register your models here.
