# Generated by Django 2.2.4 on 2019-08-09 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20190809_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='desc_en',
        ),
        migrations.RemoveField(
            model_name='document',
            name='desc_th',
        ),
    ]
