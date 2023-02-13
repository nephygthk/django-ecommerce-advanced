from uuid import uuid4
import random

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)

    # utilities
    unique_id = models.CharField(max_length=100, null=True, blank=True)
    unique_num = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        data = list(range(1000, 10000))
        random.shuffle(data)
        if self.unique_id is None:
            self.unique_id = str(uuid4()).split("-")[4]
        if self.unique_num is None:
            self.unique_num = str(data[12])
        if self.slug is None:
            self.slug = slugify("{} {} {}".format(self.name, self.unique_id, self.unique_num))
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        self.slug = slugify("{} {} {}".format(self.name, self.unique_num, self.unique_id))
        self.date_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("store:product_by_category", args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
