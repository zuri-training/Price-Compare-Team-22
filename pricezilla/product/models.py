
from django.db import models
from user.models import User

class Customer (models.Model):
    name = models.CharField(max_length=250, null=True)
    phone= models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
        class Meta:
            verbose_name_plural = "categories"

        name = models.CharField(max_length=255, default='')
        slug = models.SlugField(blank=True, default='')
    

        def __str__(self):
            return self.name

class Store(models.Model):
    name = models.CharField(max_length=255, default='')
    website = models.CharField(max_length=255, default='')
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
        name = models.CharField(max_length=255, null=True)
        slug = models.SlugField(blank=True,  null=True)
        category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
        store = models.ForeignKey(Store, null=True, on_delete=models.CASCADE)
        price = models.FloatField(null=True)
        description = models.CharField(max_length=200, null=True, blank=True)
        created_on = models.DateTimeField(auto_now_add=True, null=True)
        modified_on = models.DateTimeField(auto_now=True, null=True)
        tags = models.ManyToManyField(Tag)
        def __str__(self):
            return self.name
        
     

     
class Order(models.Model):
    STATUS = (
        ('Out of stock', 'Out of stock'),
        ('Available', "Available"),
        ('Pending', 'Pending')
    )
    
    customer = models.ForeignKey(Customer,null=True,  on_delete=models.SET_NULL) 
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    
    
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250,null=True, choices = STATUS)
    note = models.CharField(max_length=1000
, null=True)
    def __str__(self):
        return self.product.name

  

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey('Product', on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

