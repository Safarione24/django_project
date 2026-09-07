from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/new/', views.CategoryCreateView.as_view(), name='create_category'),
    path('product/new/', views.ProductCreateView.as_view(), name='create_product'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='update_category'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('category/<int:pk>/detail/', views.CategoryDetailInfoView.as_view(), name='detail_category'),
    path('category/list/', views.CategoryListView.as_view(), name='list_category'),
    path('product/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
]