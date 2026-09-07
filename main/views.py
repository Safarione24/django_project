from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from .models import Category, Product
from .forms import CategoryForm, ProductForm 

class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = 'Главная'
        return context

class CategoryDetailView(ListView):
    model = Product
    template_name = 'category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs['category_id'])
        context['title'] = f'Категория: {context["category"].name}'
        return context

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

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create_category.html'
    success_url = reverse_lazy('list_category')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "confirm_delete_category.html"
    success_url = reverse_lazy('list_category')

class CategoryDetailInfoView(DetailView):
    model = Category
    template_name = 'description_category.html'
    context_object_name = 'category'

class CategoryListView(ListView):
    model = Category
    template_name = 'list_category.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = Category.objects.order_by('name')
        
        search_field = self.request.GET.get('q')
        if search_field:
            queryset = queryset.filter(Q(name__icontains=search_field))
        
        category_filter = self.request.GET.get('category_filter')
        if category_filter and category_filter.isdigit():
            queryset = queryset.filter(id=category_filter)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        context['search_query'] = self.request.GET.get('q', '')
        context['category_filter'] = self.request.GET.get('category_filter', '')
        context['all_categories'] = Category.objects.all().order_by('name')  # Для выпадающего списка
        return context