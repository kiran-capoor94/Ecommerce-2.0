from django.urls import path, include

from .views import address_list_view, checkout_address_create_view, checkout_address_reuse_view

app_name = 'addresses'

urlpatterns = [
    path('create/', checkout_address_create_view, name='address_create'),
    path('reuse/', checkout_address_reuse_view, name='address_reuse'),
    path('', address_list_view, name='address_list'),
]