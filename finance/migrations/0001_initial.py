# Generated by Django 2.2.4 on 2019-08-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.TextField()),
                ('title_th', models.TextField(blank=True, default='')),
                ('content_en', models.TextField()),
                ('content_th', models.TextField(blank=True, default='')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
