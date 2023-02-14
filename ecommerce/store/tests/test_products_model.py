from django.db import IntegrityError
import pytest

from ecommerce.store.models import Product


def test_product_entry(db, single_product):
    new_product = single_product
    assert new_product.name == 'iphone6'
    assert new_product.category.name == 'Electronics'


def test_product_entry_factoryboy(db, product_factory):
    new_product = product_factory.create()
    assert new_product.name == 'iphone6'
    assert new_product.category.name == 'fashion'


def test_product_return_str(db, single_product):
    new_product = single_product
    assert new_product.__str__() == 'iphone6'


def test_product_return_str_factoryboy(db, product_factory):
    new_product = product_factory.create()
    assert new_product.__str__() == 'iphone6'


@pytest.mark.parametrize(
    "name, web_id, unique_id",
    [
        ("iphone6","7890","unr894747")
    ], )
def test_product_entry_generate_slug(db, single_category, name, web_id, unique_id):
    new_category = single_category
    new_product = Product.objects.create(name=name, web_id=web_id, unique_id=unique_id,
                                        category=new_category)
    assert new_product.slug == 'iphone6-7890-unr894747'
    assert new_product.web_id == "7890"


@pytest.mark.parametrize(
    "name, web_id, unique_id",
    [
        ("iphone6","7890","unr894747")
    ], )
def test_product_entry_generate_slug_factoryboy(db, product_factory, name, web_id, unique_id):
    new_product = product_factory.create(name=name, web_id=web_id, unique_id=unique_id,)
    assert new_product.slug == 'iphone6-7890-unr894747'
    assert new_product.web_id == "7890"



def test_product_inventory_entry_factoryboy(db, product_inventory_factory):
    new_product_inventory = product_inventory_factory.create(sku="123456789", store_price=20000)
    assert new_product_inventory.sku == "123456789"
    assert new_product_inventory.store_price == 20000
    assert new_product_inventory.product.name == "iphone6"


def test_product_inventory_return_str_factoryboy(db, product_inventory_factory):
    new_product_inventory = product_inventory_factory.create()
    assert new_product_inventory.__str__() == "iphone6"


def test_product_inventory_sku_and_upi_uniqueness_factoryboy(db, product_inventory_factory):
    new_product_inventory = product_inventory_factory.create(sku="123456789", upi="2345")
    with pytest.raises(IntegrityError):
        product_inventory_factory.create(sku="123456789", upi="2345")
    