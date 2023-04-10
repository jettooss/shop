from django.contrib import admin
from .models import *
# Register your models here.
from image_uploader_widget.admin import ImageUploaderInline


# class ProductImageAdmin(ImageUploaderInline):
#     model = product_main


@admin.register(product_main)
class Product_main_admin(admin.ModelAdmin):
    list_display = [ 'product', "image"]
    # inlines = [ProductImageAdmin]
@admin.register(Product_category)
class Product_category_admin(admin.ModelAdmin):
        list_display = ['category_name']


# #   category = models.ForeignKey(Product_category, on_delete=models.CASCADE, verbose_name="category")
#     name=models.CharField(max_length=100, verbose_name='Название')
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
@admin.register(Label_Product)
class Label_Product_admin(admin.ModelAdmin):
        list_display = ['pk','name']
        search_fields = ['name']
        prepopulated_fields = {"slug" :("name",)}

@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = [ 'category' , 'name','image','description','price','created','updated','s','m','l','xl']




