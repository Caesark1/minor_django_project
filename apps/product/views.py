from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product, slug=slug)


class CategoryDetailView(DetailView):
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

    def get_object(self):
        slug = self.kwargs.get('slug')
        # print(Category.objects.get(slug='smartphone'))
        return get_object_or_404(Category, slug=slug)
