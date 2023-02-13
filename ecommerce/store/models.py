import random
from uuid import uuid4
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

from ecommerce.category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='name', help_text='Required')
    web_id = models.CharField(unique=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='description', help_text='Not required')
    store_price = models.IntegerField(verbose_name='Regular price', help_text='price must not be less than 0')
    discount_price = models.IntegerField(verbose_name='Discount price', help_text='price must not be less than 0')
    is_active = models.BooleanField(defult=True)

    # relations
    category = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE)

    # utilities
    unique_id = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        data = list(range(1000, 10000))
        random.shuffle(data)
        if self.unique_id is None:
            self.unique_id = str(uuid4()).split("-")[4]
        if self.web_id is None:
            self.web_id= str(data[12])
        if self.slug is None:
            self.slug = slugify("{} {} {}".format(self.name,self.web_id, self.unique_id))
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        self.slug = slugify("{} {} {}".format(self.name, self.web_id, self.unique_id))
        self.date_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
