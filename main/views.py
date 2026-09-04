from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Category, Product
from .forms import CategoryForm, ProductForm 

class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        return super().get_context_data(categories=Category.objects.all(), **kwargs)

class CategoryDetailView(ListView):
    model = Product
    template_name = 'category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id'])

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'create_category.html'
    success_url = reverse_lazy('index')

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('index')

class ProductDetailView(DetailView): 
    model = Product
    template_name = 'product_detail.html' 
    context_object_name = 'product'      
    pk_url_kwarg = 'product_id'           

# class CategoryDetailView(DetailView):
#     model = Category
#     context_object_name = 'category'