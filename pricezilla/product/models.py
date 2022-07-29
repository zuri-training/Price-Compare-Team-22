from django.db import models
from user.models import User

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


class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField(max_length = 200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.name)

