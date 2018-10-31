from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from ecommAppCFE.utils import unique_slug_generator

# import os
# import random

# def get_filename_ext(filename):
#     base_name = os.path.basename(filename)
#     name, ext = os.path.splitext(base_name)
#     return name, ext

# def upload_image_path(instance, filename):
#     print(instance)
#     print(filename)
#     new_filename = random.randint(1,316384351)
#     name, ext = get_filename_ext(filename)
#     final_filename = '{new_dilename}{ext}'.format(new_filename=new_filename, ext=ext)
#     return "products/%Y/%m/%d/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Custom Query Set 
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Product(models.Model):
    objects = ProductManager()

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.01)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    # stock = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_digital = models.BooleanField(default=False) # User Library
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={'slug': self.slug})

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_reciever, sender=Product)
