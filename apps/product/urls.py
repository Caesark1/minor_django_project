from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name = 'index'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('<str:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('categories/<str:slug>', views.CategoryDetailView.as_view(), name='category_detail')
]
