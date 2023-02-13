from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView , ListView, TemplateView

from ecommerce.category.models import Category
from .models import Product


# class ProductByCategory(View):
#     model = Product
#     template_name = "store/store.html"
#     context_object_name = 'products'

#     def get_queryset(self, slug):
#         category = get_object_or_404(Category, slug=slug)
#         qs = super(ProductByCategory, self,).get_queryset()
#         qs = qs.filter(category=category)
#         return qs
    
class ProductByCategory(View):
    def get(self, request, slug):
        category = get_object_or_404(Category,slug=slug)
        products = Product.objects.filter(category=category)

        context = {'products':products, 'category':category}

        return render(request, "store/store.html", context )
