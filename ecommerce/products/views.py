from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Product


# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/product_list.html"


class ProductFeaturedView(ListView):
    queryset = Product.objects.filter(featured=True, active=True)
    template_name = "products/product_featured.html"


class ProductDetailView(DetailView):
    model = Product


class ProductDetailSlugView(DetailView):
    model = Product
