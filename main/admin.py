from django.contrib import admin
from .models import *
# Register your models here.
from image_uploader_widget.admin import ImageUploaderInline


class ProductImageAdmin(ImageUploaderInline):
    model = product_main


@admin.register(product_main)
class product_main_admin(admin.ModelAdmin):
    list_display = ( 'product', "image")
    # inlines = [ProductImageAdmin]
