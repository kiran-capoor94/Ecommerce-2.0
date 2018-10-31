from django.urls import path, include

from .views import SearchProductListView

app_name ='search'

urlpatterns = [
    path('',SearchProductListView.as_view(), name='query'),
]