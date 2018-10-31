from django.urls import path, include

from .views import home_page, about_page, contact_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path('cart/', include('carts.urls', namespace='carts')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('address/', include('addresses.urls', namespace='addresses')),
]