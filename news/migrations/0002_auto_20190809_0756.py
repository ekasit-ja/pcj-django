# Generated by Django 2.2.4 on 2019-08-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='code_en',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='code_th',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
