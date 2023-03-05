from django.db import models

# Create your models here.
class product_main(models.Model):

    product = models.CharField(max_length=100, verbose_name='Название')

    image = models.ImageField(verbose_name="image",upload_to='main/static/images/')