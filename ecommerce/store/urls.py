from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('<slug:slug>', views.ProductByCategory.as_view(), name="product_by_category"),
    path('detail/<slug:slug>', views.ProductDetailView.as_view(), name="product_detail"),
]

