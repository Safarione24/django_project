from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/new/', views.CategoryCreateView.as_view(), name='create_category'),
    path('product/new/', views.ProductCreateView.as_view(), name='create_product'),
    path('delete_category/<int> update_category/new/', views.CategoryUpdatelView.as_view(), name='update_category'),

]
