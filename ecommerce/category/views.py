from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView
from django.views.generic.base import View

from ecommerce.category.models import Category, SubCategory


# class CategoryList(View):
#     def get(self, request, slug):
#         category = get_object_or_404(Category, slug=slug)
#         sub_categories = SubCategory.objects.filter(category=category)
#         context = {
#             'category': category,
#             'sub_categories': sub_categories,
#         }
#         return render(request, 'category/category_list.html', context)




