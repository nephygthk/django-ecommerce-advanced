import pytest
# from django.utils import timezone

from ecommerce.category.models import Category, Brand


@pytest.fixture
def single_category(db):
    category = Category.objects.create(name="Electronics", unique_id="eaerti123",
                                       unique_num="2098")
    return category


@pytest.fixture
def single_brand(db):
    brand = Brand.objects.create(name="Samsung", slug="samsung")
    return brand
