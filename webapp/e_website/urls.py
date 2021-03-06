"""e_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',home,name='home'),
    url('^oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    url(r'^logout/$',logout_app,name='logout'),
    url(r'^products/$', all_products, name='all_products'),
    # url(r'^product/(?P<id>\d+)/$', product, name='product'),
    url(r'^add_to_cart/product/(?P<id>\d+)/$', add_to_cart, name='add_to_cart'),
    url(r'^remove_cart/(?P<id>\d+)', remove_cart, name='remove_cart'),
    url(r'^add_address/$', add_address, name='add_address'),
    url(r'^my_orders/$', my_orders, name='my_orders'),
    # url(r'^cart/$', cart_empty, name='cart_empty'),
    url(r'^buyer_tq/$', buyer_tq, name='buyer_tq'),
    url(r'^cartpage/$', cartpage, name='cartpage'),
    url(r'^address_form/$', address_form, name='address_form'),
    url(r'^receipt/$', receipt, name='receipt'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


