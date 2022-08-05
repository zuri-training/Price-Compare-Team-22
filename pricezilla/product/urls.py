
from django.urls import path
from .import views

urlpatterns = [
path('sign-up/', views.signUp, name="signup"),
path('login/', views.LogIn, name ='login' ),
path('products/', views.home,  name='product_list'),
path('laptops/', views.laptop, name='laptop' ),
path('customer/<str:pk_test>/', views.customer, name='customer'),
path('dashboard/', views.dashboard, name='dashboard'),
path('create_order/<str:pk>/', views.createOrder, name='create_order'),
path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
path('', views.apiOverview, name = 'api-overview'),
path('product-list/', views.productList, name='product-list' ),
path('product-detail/<str:pk>/', views.productDetail, name='product-list' ),
path('product-create/', views.productCreate, name="product-create"),
path('product-update/<str:pk>/', views.productUpdate, name="product-update"),
path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),


    
]