import pytest

from ecommerce.store.models import Product


@pytest.fixture
def single_product(db, single_category):
    new_category = single_category
    new_product = Product.objects.create(name="iphone6", category=new_category)
    return new_product


# @pytest.fixture
# def single_product_inventory(db, single_product):
#     new_product = single_product
#     new_product_inventory = Product.objects.create(sku="123456789", upi="ght90987",
#                                                 store_price=20000, sale_price=18000,
#                                                 product=new_product)
#     return new_product_inventory

