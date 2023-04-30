from django.contrib import admin
from .models import *
# Register your models here.
from image_uploader_widget.admin import ImageUploaderInline




@admin.register(product_main)
class Product_main_admin(admin.ModelAdmin):
    list_display = [ 'product', "image"]
    # inlines = [ProductImageAdmin]
@admin.register(Product_category)
class Product_category_admin(admin.ModelAdmin):
        list_display = ['category_name']


@admin.register(Label_Product)
class Label_Product_admin(admin.ModelAdmin):
        list_display = ['pk','name']
        search_fields = ['name']
        prepopulated_fields = {"slug" :("name",)}

@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = [ 'category' , 'name','image','description','price','created','updated','s','m','l','xl']

@admin.register(Basket)
class Basket_admin(admin.ModelAdmin):
    list_display = ['id', 'user' , 'name','price','created']
@admin.register(Order)

class Order_admin(admin.ModelAdmin):
    list_display = ['user']

