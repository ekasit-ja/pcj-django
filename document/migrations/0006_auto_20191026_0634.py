# Generated by Django 2.2.4 on 2019-10-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0005_auto_20190810_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('cert', 'Certificate'), ('inst', 'Installation'), ('catg', 'Catalog')], default='cert', max_length=5),
        ),
        migrations.AlterField(
            model_name='document',
            name='product_type',
            field=models.CharField(choices=[('frd', 'Fire Doors'), ('fdc', 'Fire Dampers'), ('fsd-ul', 'Fire & Smoke Dampers'), ('ddp', 'Duct Dampers'), ('ds', 'Duct Silencers'), ('aol', 'Air Outlets'), ('dhw', 'Door Hardware')], default='frd', max_length=5),
        ),
    ]
