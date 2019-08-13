# Generated by Django 2.2.4 on 2019-08-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='desc_en',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='desc_th',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='title_th',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.CharField(max_length=10),
        ),
    ]
