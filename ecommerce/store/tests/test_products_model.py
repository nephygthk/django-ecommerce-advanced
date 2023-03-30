from django.db import IntegrityError
import pytest
from ecommerce.store import models

from ecommerce.store.models import Product


def test_product_entry(db, product_factory):
    new_product = product_factory.create()
    assert new_product.name == 'iphone6'
    assert new_product.category.name == 'fashion'


def test_product_return_str(db, product_factory):
    new_product = product_factory.create()
    assert new_product.__str__() == 'iphone6'


@pytest.mark.parametrize(
    "name, web_id, unique_id",
    [
        ("iphone6","7890","unr894747")
    ], )
def test_product_entry_generate_slug(db, product_factory, name, web_id, unique_id):
    new_product = product_factory.create(name=name, web_id=web_id, unique_id=unique_id,)
    assert new_product.slug == 'iphone6-7890-unr894747'
    assert new_product.web_id == "7890"


def test_product_attribute_entry_and_return_str(db, product_attribute_factory):
    new_product_attribute = product_attribute_factory.create(name="color")
    assert new_product_attribute.name == 'color'
    assert new_product_attribute.__str__() == 'color'
    

def test_product_attribute_name_uniqueness(db, product_attribute_factory):
    new_product_attribute = product_attribute_factory.create(name="color")
    with pytest.raises(IntegrityError):
        product_attribute_factory.create(name="color")


def test_product_attribute_value_entry(db, product_attribute_value_factory):
    new_product_attribute_value = product_attribute_value_factory.create(product_attribute__name="color")
    assert new_product_attribute_value.product_attribute.name == 'color'
    assert new_product_attribute_value.attribute_value == 'red'


def test_product_type_data_entry_and_return_str(db, product_type_factory):
    new_product_type = product_type_factory.create(name="phone")
    assert new_product_type.name == "phone"
    assert new_product_type.__str__() == "phone"

def test_product_type_name_uniqueness(db, product_type_factory):
    new_product_type = product_type_factory.create(name="phone")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="phone")


def test_product_type_insert_product_attribute_data(db, product_type_with_attribute_factory):
    new_product_type_attribute = product_type_with_attribute_factory(id=1)
    result = models.ProductType.objects.get(id=1)
    count = result.product_type_attributes.all().count()
    assert count == 2

def test_product_inventory_entry(db, product_inventory_factory):
    new_product_inventory = product_inventory_factory.create(sku="123456789", store_price=20000)
    assert new_product_inventory.sku == "123456789"
    assert new_product_inventory.store_price == 20000
    assert new_product_inventory.product.name == "iphone6"


def test_product_inventory_return_str(db, product_inventory_factory):
    new_product_inventory = product_inventory_factory.create()
    assert new_product_inventory.__str__() == "iphone6"


def test_product_inventory_sku_and_upi_uniqueness(db, product_inventory_factory):
    new_product_inventory = product_inventory_factory.create(sku="123456789", upi="2345")
    with pytest.raises(IntegrityError):
        product_inventory_factory.create(sku="123456789", upi="2345")


def test_product_inventory_insert_product_attribute_values(db, product_with_attribute_values_factory):
    new_product_inventory_attribute = product_with_attribute_values_factory(sku="66778899")
    result = models.ProductInventory.objects.get(sku="66778899")
    count = result.attribute_values.all().count()
    assert count == 4


def test_product_media_data_entry(db, media_factory):
    new_image = media_factory.create(product_inventory__upi="22334455")
    assert new_image.img_url == "images/phone.png"
    assert new_image.product_inventory.upi == "22334455"
    assert new_image.is_feature == 1


def test_stock_data_entry_and_return_str(db, stock_factory):
    new_stock = stock_factory(product_inventory__upi="22334455",product_inventory__product__name = "shoe")
    assert new_stock.units == 2
    assert new_stock.units_sold == 100
    assert new_stock.product_inventory.upi == "22334455"
    assert new_stock.__str__() == "shoe"