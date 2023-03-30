import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

from ecommerce.category.models import Category, Brand
from ecommerce.store import models
fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "fashion"
    unique_id = "eaty2233"
    unique_num = "1234"


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = "samsung"
    slug = "samsung"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = "iphone6"
    category = factory.SubFactory(CategoryFactory)


class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttribute

    name = factory.Sequence(lambda n: "attribute_name_%d" % n)


class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttributeValue

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value = "red"


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductType

    name = factory.Sequence(lambda n: "type_%d" % n)


class ProductTypeAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductTypeAttribute

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    product_type = factory.SubFactory(ProductTypeFactory)


class ProductTypeWithAttributeFactory(ProductTypeFactory):
    product_attribute1 = factory.RelatedFactory(ProductTypeAttributeFactory, factory_related_name="product_type",)
    product_attribute2 = factory.RelatedFactory(ProductTypeAttributeFactory, factory_related_name="product_type",)


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductInventory

    sku = factory.Sequence(lambda n: "sku_%d" % n)
    upi = factory.Sequence(lambda n: "upi_%d" % n)
    product = factory.SubFactory(ProductFactory)
    brand = factory.SubFactory(BrandFactory)
    product_type = factory.SubFactory(ProductTypeFactory)
    is_active = 1
    store_price = 80000
    sale_price = 53000


class ProductAttributeValuesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttributeValues

    attributevalues = factory.SubFactory(ProductAttributeValueFactory)
    productinventory = factory.SubFactory(ProductInventoryFactory)


class ProductWithAttributeValuesFactory(ProductInventoryFactory):
    attributevalues1 = factory.RelatedFactory(ProductAttributeValuesFactory,
                                            factory_related_name="productinventory",)
    attributevalues2 = factory.RelatedFactory(ProductAttributeValuesFactory,
                                            factory_related_name="productinventory",)
    attributevalues3 = factory.RelatedFactory(ProductAttributeValuesFactory,
                                            factory_related_name="productinventory",)
    attributevalues4 = factory.RelatedFactory(ProductAttributeValuesFactory,
                                            factory_related_name="productinventory",)
    

class MediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Media

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    img_url = "images/phone.png"
    alt_text = "phone image"
    is_feature = True


class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Stock

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    units = 2
    units_sold = 100




register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductInventoryFactory)
register(ProductAttributeFactory)
register(ProductAttributeValueFactory)
register(ProductTypeFactory)
register(ProductTypeAttributeFactory)
register(ProductTypeWithAttributeFactory)
register(ProductAttributeValuesFactory)
register(ProductWithAttributeValuesFactory)
register(MediaFactory)
register(StockFactory)

