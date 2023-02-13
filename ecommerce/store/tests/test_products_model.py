import pytest


def test_product_entry(db, single_product):
    new_product = single_product
    assert new_product.name == 'iphone6'
    assert new_product.category.name == 'Electronics'


def test_product_return_str(db, single_product):
    new_product = single_product
    assert new_product.__str__() == 'iphone6'
