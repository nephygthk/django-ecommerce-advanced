import random
from uuid import uuid4
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

from ecommerce.category.models import Category, Brand


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='name', help_text='Required')
    web_id = models.CharField(unique=True, max_length=80, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='description', help_text='Not required', null=True, blank=True)
    image = models.ImageField(upload_to="product_image/", default="product_image/default.png")
    main_price = models.IntegerField(verbose_name='main price', help_text='price must not be less than 0')

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
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class ProductAttribute(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="format: required, unique, max-255")
    description = models.TextField(null=True, blank=True, help_text="format: not required")

    def __str__(self):
        return self.name
    
class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(ProductAttribute, related_name="product_attribute",
                                        on_delete=models.PROTECT)
    attribute_value = models.CharField(max_length=200, verbose_name="attribute value",
                                    help_text="format: required, max-length=200 characters")
    
    def __str__(self):
        return self.attribute_value
    

class ProductType(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="type of product",
                            help_text="format: required, must be unique, max of 200 characters")
    product_type_attributes = models.ManyToManyField(ProductAttribute,
                                                    related_name="product_type_attributes",
                                                    through="ProductTypeAttribute")
    
    def __str__(self):
        return self.name
    

class ProductTypeAttribute(models.Model):
    product_attribute =  models.ForeignKey(ProductAttribute, related_name="productattribute",
                                           on_delete=models.PROTECT)
    product_type =  models.ForeignKey(ProductType, related_name="producttype",
                                           on_delete=models.PROTECT)
    
    class Meta:
        unique_together = (("product_attribute", "product_type"),)        
    

class ProductInventory(models.Model):
    sku = models.CharField(max_length=20, unique=True, help_text="stock keeping price", null=True)
    upi = models.CharField(max_length=30, unique=True, help_text="universal product id", null=True)
    store_price = models.IntegerField(verbose_name='Regular store price', help_text='price must not be less than 0')
    sale_price = models.IntegerField(verbose_name='sale price', help_text='price must not be less than 0')
    is_active = models.BooleanField(default=True, verbose_name="product visibility", help_text="checking: True= Product visible")
    is_default = models.BooleanField(default=False, verbose_name="default selection", help_text="Format: true= sub product selected")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="date sub-product created")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date sub-product updated")

    # relations
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, related_name="product_type",
                                    on_delete=models.PROTECT)
    attribute_values = models.ManyToManyField(ProductAttributeValue,
                                            related_name="product_attribute_values",
                                            through="ProductAttributeValues",)

    def __str__(self):
        return self.product.name
    

class ProductAttributeValues(models.Model):
    attributevalues = models.ForeignKey(ProductAttributeValue,
                                        related_name="attributevaluevalues",
                                        on_delete=models.PROTECT,)
    productinventory = models.ForeignKey(ProductInventory,
                                        related_name="productattributevaluevalues",
                                        on_delete=models.PROTECT,)
    
    class Meta:
        unique_together = (("attributevalues", "productinventory"),)

    def __str__(self):
        return self.attributevalues.attribute_value


class Media(models.Model):
    product_inventory = models.ForeignKey(ProductInventory,
                                        related_name="media_product_inventory",
                                        on_delete=models.PROTECT,)
    img_url = models.ImageField(verbose_name="product image", upload_to="product_image/",
                                default="product_image/default.png",help_text="format: required, default-default.png")
    alt_text = models.CharField(max_length=255, verbose_name="alternative text",
                                help_text="format: required, max-255")
    is_feature = models.BooleanField(default=False, verbose_name="product default image",)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product image"
        verbose_name_plural = "product images"


class Stock(models.Model):
    product_inventory = models.OneToOneField(ProductInventory,
                        related_name="product_inventory", on_delete=models.PROTECT)
    last_checked = models.DateTimeField(null=True, blank=True,
                    verbose_name="inventory last stock check date")
    units = models.IntegerField(default=0, verbose_name="units/qty of stock")
    units_sold = models.IntegerField(default=0, verbose_name="units sold to date")

    def __str__(self):
        return self.product_inventory.product.name
    
