from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):
    template_name = "products/product_list.html"
    model = Product

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q') or ''
        print(f'query: {query}')
        return Product.objects.filter(title__icontains=query)
