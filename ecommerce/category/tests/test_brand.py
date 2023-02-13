import pytest
from django.db import IntegrityError

from ecommerce.category.models import Brand


def test_single_brand_entry(db, single_brand):
    new_brand = single_brand
    assert new_brand.name == "Samsung"
    assert new_brand.slug == "samsung"


def test_brand_return_str(db, single_brand):
    new_brand = single_brand
    assert new_brand.__str__() == "Samsung"


@pytest.mark.parametrize(
    "name, slug",
    [
        ("Samsung", "samsung"),
    ], )
def test_brand_unique_constraint(db, single_brand, name, slug):
    with pytest.raises(IntegrityError) as e:
        new_brand = single_brand
        new_brand2 = Brand.objects.create(name=name, slug=slug)
