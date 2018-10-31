from django.urls import path, include

from .views import ProductListView, ProductDetailSlugView

app_name ='products'

urlpatterns = [
    path('',ProductListView.as_view(), name='list'),
    path('<slug>/',ProductDetailSlugView.as_view(), name='detail'),
]