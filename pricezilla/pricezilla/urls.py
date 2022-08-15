
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('get-help/', views.gethelp, name='gethelp'),
    path('sign-up/', views.signup, name='signup'),
    path('get-started/', views.getstarted,name='getstarted'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('how-to-show-reviews/', views.howreviews, name='howreviews'),
    path('contactpricezilla/', views.contactpricezilla, name='contactpricezilla'),
    path('documentation/', views.documentation, name='documentation'),
    path('register-shop/', views.registershop, name='registershop'),
    path('rulesandguide/', views.rulesandguide, name='rulesandguide'),
    path('profile/', views.profile, name='profile'),
    path('unauthenticated-signup/', views.unauthenticated, name='unauthenticated'),
    path('contact/',views.contact, name="contact"),
    path('startcompare/', views.startcomparing, name='startcompare'),
    path('account/', views.account, name='account'),
    path('search/', views.searchbar, name='search'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('user.urls')),
    path('product/', include('product.urls')),
    path('promo/', views.promodeal, name='promo'),
    path('faq/', views.faq, name='faq')

]

urlpatterns += staticfiles_urlpatterns()
