# Generated by Django 4.1.3 on 2023-01-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(default='test', max_length=45, unique=True),
            preserve_default=False,
        ),
    ]
