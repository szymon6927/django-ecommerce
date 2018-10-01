from django.conf.urls import url
from .views import ProductListView, ProductDetailView, ProductDetailSlugView, ProductFeaturedView


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^featured/$', ProductFeaturedView.as_view(), name='products-featured'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='product-slug'),
]