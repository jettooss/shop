# Generated by Django 4.1.7 on 2023-03-05 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_main',
            name='image',
            field=models.ImageField(upload_to='main/static/images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product_main',
            name='product',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]