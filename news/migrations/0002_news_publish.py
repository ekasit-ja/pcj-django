# Generated by Django 2.1.14 on 2023-05-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
