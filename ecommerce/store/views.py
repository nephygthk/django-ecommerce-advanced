from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView , ListView, TemplateView

from ecommerce.category.models import Category
from .models import Product, ProductInventory

   
class ProductByCategory(DetailView):
    model = Category
    template_name = 'store/store.html'
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductByCategory,
             self).get_context_data(*args, **kwargs)
        
        category = context["category"]
        context["products"] = Product.objects.filter(category=category)  
        # context["products"] = ProductInventory.objects.filter(product__category=category).filter(is_default=True)    
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView,
             self).get_context_data(*args, **kwargs)
        
        product = context["product"]
        context["product_inventory"] = ProductInventory.objects.filter(product=product).filter(is_default=True)
        return context

# class ProductByCategory(View):
#     def get(self, request, slug):
#         category = get_object_or_404(Category,slug=slug)
#         products = Product.objects.filter(category=category)

#         context = {'products':products, 'category':category}

#         return render(request, "store/store.html", context )
