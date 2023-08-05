from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from .models import Group, Manufacturer, Product


class ProductContext:
    """
     Группы и производителя товаров
    """

    def get_groups(self):
        return Group.objects.all()
    
    def get_manufacturers(self):
        return Manufacturer.objects.all()


class ProductListView(ProductContext, ListView):
    
    model = Product
    paginate_by = 1
    template_name = 'test.html'