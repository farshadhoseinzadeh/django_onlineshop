from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.filter(active=True).order_by('-datetime_modified')
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    # paginate_by = 6


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
