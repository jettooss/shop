from _pydecimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class product_main(models.Model):
    product = models.CharField(max_length=100, verbose_name='Название')

    image = models.ImageField(verbose_name="image", upload_to='main/static/images/')


class Product_category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='название категории', primary_key=True)

    class Meta:
        verbose_name_plural = 'категории '


class Label_Product(models.Model):
    category = models.ForeignKey(Product_category, on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(max_length=100, verbose_name='Название', primary_key=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Label_Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, primary_key=True)
    image = models.ImageField(upload_to='products/static/images/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)



    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    xs = models.IntegerField(default=0)
    s = models.IntegerField(default=0)
    m = models.IntegerField(default=0)
    l = models.IntegerField(default=0)
    xl = models.IntegerField(default=0)


user = get_user_model()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    Status = (
        ('a', 'В обработке'),
        ('b', 'Доставляется'),
        ('c', 'Выполнен '),
    )
    status = models.CharField(choices=Status, verbose_name="статус", max_length=1, default="a")

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=Basket.Status, verbose_name="статус", max_length=1, default="c")
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)