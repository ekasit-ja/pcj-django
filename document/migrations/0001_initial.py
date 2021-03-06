# Generated by Django 2.2.4 on 2019-08-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=255)),
                ('title_th', models.CharField(blank=True, max_length=255)),
                ('desc_en', models.TextField(blank=True, default='')),
                ('desc_th', models.TextField(blank=True, default='')),
                ('image', models.ImageField(upload_to='document')),
                ('doc_en', models.FileField(upload_to='document')),
                ('doc_th', models.FileField(upload_to='document')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
