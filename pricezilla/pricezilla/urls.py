
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('sign-up/', views.signup, name='signup'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('how-to-show-reviews/', views.howreviews, name='howreviews'),
    path('contactpricezilla/', views.contactpricezilla, 'contactpricezilla'),
    path('profile/', views.profile, name='profile'),
    path('contact/',views.contact, name="contact"),
    path('account/', views.account, name='account'),
    path('search/', views.searchbar, name='search'),
    path('accounts/', include('user.urls')),
    path("accounts/",include("django.contrib.auth.urls")),
    # path('accounts/', include('allauth.urls')),
    path('product/', include('product.urls')),

]

urlpatterns += staticfiles_urlpatterns()
