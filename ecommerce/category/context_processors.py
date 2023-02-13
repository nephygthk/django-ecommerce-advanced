from django.shortcuts import get_object_or_404

from .models import Category


def categories(request):
    all_categories = Category.objects.all()
    return {"categories": all_categories}


