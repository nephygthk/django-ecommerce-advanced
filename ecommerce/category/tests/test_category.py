import pytest
from django.db import IntegrityError
from django.utils import timezone

from ecommerce.category.models import Category


def test_category_entry(db, category_factory):
    new_category = category_factory.create()
    assert new_category.slug == "fashion-1234-eaty2233"
    assert new_category.name == "fashion"
    assert new_category.unique_id == "eaty2233"
    assert new_category.unique_num == "1234"


def test_category_model_return_str(db, category_factory):
    new_category = category_factory.create()
    assert new_category.__str__() == "fashion"


@pytest.mark.parametrize(
    "name, unique_id, unique_num",
    [
        ("fashion", "eaty2233", "1234"),
    ], )
def test_category_name_unique_constraint(db, category_factory, name, unique_id, unique_num):
    new_category = category_factory.create()
    with pytest.raises(IntegrityError) as e:
        category_factory.create(name=name, unique_id=unique_id, unique_num=unique_num)


@pytest.mark.parametrize(
    "name",
    [
        "fashion"
    ], )
def test_category_unique_id_and_num_is_none(db,name, category_factory):
    new_category = category_factory.create(name=name, unique_id=None, unique_num=None)
    assert new_category.name == 'fashion'

