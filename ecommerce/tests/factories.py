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


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductInventory

    sku = factory.Sequence(lambda n: "sku_%d" % n)
    upi = factory.Sequence(lambda n: "upi_%d" % n)
    product = factory.SubFactory(ProductFactory)
    is_active = 1
    store_price = 80000
    sale_price = 53000




register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductInventoryFactory)

