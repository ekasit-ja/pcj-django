# Generated by Django 2.2.4 on 2019-08-09 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190809_0832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_choice',
            new_name='product_type',
        ),
    ]
