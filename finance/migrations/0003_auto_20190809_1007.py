# Generated by Django 2.2.4 on 2019-08-09 10:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20190809_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
