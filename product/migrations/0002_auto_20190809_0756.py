# Generated by Django 2.2.4 on 2019-08-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc_en',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='desc_th',
            field=models.TextField(default=''),
        ),
    ]
