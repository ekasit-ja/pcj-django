# Generated by Django 2.2.4 on 2019-08-10 03:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20190809_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc_en',
            field=ckeditor.fields.RichTextField(blank=True, default='', verbose_name='description english'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc_th',
            field=ckeditor.fields.RichTextField(blank=True, default='', verbose_name='description thai'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name='title english'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_th',
            field=models.CharField(blank=True, max_length=255, verbose_name='title thai'),
        ),
    ]
