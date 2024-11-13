from django.views import generic
from django.shortcuts import get_object_or_404, reverse

from .models import Product, Comment
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context_object_name = super().get_context_data(**kwargs)
        context_object_name['comment_form'] = CommentForm()
        return context_object_name


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        return super().form_valid(form)
