from django.contrib import admin

from ecommerce.category.models import Brand
from ecommerce.store.models import (
    Product,
    Stock,
    ProductAttribute,
    ProductType,
    ProductInventory,
    ProductAttributeValue,
    Media,
    ProductAttributeValues,
    ProductTypeAttribute)


class ProductTypeInline(admin.TabularInline):
    model = ProductType.product_type_attributes.through


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue

class ProductTypeAttributeInline(admin.TabularInline):
    model = ProductTypeAttribute


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    inlines = [
        ProductAttributeValueInline,
        ProductTypeAttributeInline
    ]


class ProductInventoryInline(admin.TabularInline):
    model = ProductInventory

class MediaInline(admin.TabularInline):
    model = Media


class StockInline(admin.TabularInline):
    model = Stock


class ProductAttributeValuesInline(admin.TabularInline):
    model = ProductAttributeValues
    extra = 1


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [
        MediaInline,
        StockInline,
        ProductAttributeValuesInline,
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInventoryInline,
    ]

admin.site.register(ProductType)
