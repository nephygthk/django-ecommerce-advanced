import pytest
from django.urls import reverse, NoReverseMatch


# def test_category_absolute_url(db, single_category, client):
#     new_category = single_category
#     slug = new_category.slug
#     url = reverse("category:sub_categories", args=[slug])
#     response = client.get(url)
#     assert response.status_code == 200


# def test_sub_category_page_access_with_no_args_error(db, client):
#     with pytest.raises(NoReverseMatch) as e:
#         url = reverse("category:sub_categories")
#         response = client.get(url)
