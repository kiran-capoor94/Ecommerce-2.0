from django.urls import path, include

from .views import cart_home, cart_update, checkout_home, checkout_done_view, cart_detail_api_view

app_name ='carts'

urlpatterns = [
    path('api/cart/', cart_detail_api_view, name="api-cart"),
    path('',cart_home, name='home'),
    path('checkout/', checkout_home, name='checkout'),
    path('update/', cart_update, name='update'),
    path('checkout/success/', checkout_done_view, name='success'),
]