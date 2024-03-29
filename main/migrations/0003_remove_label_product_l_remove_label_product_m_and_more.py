# Generated by Django 4.1.7 on 2023-04-10 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label_product',
            name='l',
        ),
        migrations.RemoveField(
            model_name='label_product',
            name='m',
        ),
        migrations.RemoveField(
            model_name='label_product',
            name='s',
        ),
        migrations.RemoveField(
            model_name='label_product',
            name='xl',
        ),
        migrations.RemoveField(
            model_name='label_product',
            name='xs',
        ),
        migrations.AddField(
            model_name='product',
            name='l',
            field=models.IntegerField(default=34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='m',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='s',
            field=models.IntegerField(default=34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='xl',
            field=models.IntegerField(default=343),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='xs',
            field=models.IntegerField(default=34),
            preserve_default=False,
        ),
    ]
