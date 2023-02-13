import pytest
from django.db import IntegrityError
from django.utils import timezone

from ecommerce.category.models import Category


def test_category_entry(db, single_category):
    new_category = single_category
    assert new_category.slug == "electronics-2098-eaerti123"
    assert new_category.name == "Electronics"
    assert new_category.unique_id == "eaerti123"
    assert new_category.unique_num == "2098"
    # assert new_category.date_created == timezone.localtime(timezone.now())


def test_category_model_return_str(db, single_category):
    new_category = single_category
    assert new_category.__str__() == "Electronics"


@pytest.mark.parametrize(
    "name, unique_id, unique_num",
    [
        ("Electronics", "eaerti123", "2098"),
    ], )
def test_category_name_unique_constraint(db, single_category, name, unique_id, unique_num):
    with pytest.raises(IntegrityError) as e:
        new_category = single_category
        new_category2 = Category.objects.create(name="Electronics", unique_id="eaerti123",
                                                unique_num="2098")


@pytest.mark.parametrize(
    "name",
    [
        "Electronics"
    ], )
def test_category_unique_id_and_num_is_none(db,name):
    new_category = Category.objects.create(name=name)
    assert new_category.name == 'Electronics'

