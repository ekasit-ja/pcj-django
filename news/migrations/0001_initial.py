# Generated by Django 2.2.4 on 2019-08-09 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=512)),
                ('title_th', models.CharField(max_length=512)),
                ('content_en', models.TextField()),
                ('content_th', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'news',
                'ordering': ('-order',),
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news')),
                ('order', models.PositiveIntegerField(default=0)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.News')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
