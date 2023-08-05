from django.urls import path

from .views import ProductListView

app_name = 'shop'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product'),
]