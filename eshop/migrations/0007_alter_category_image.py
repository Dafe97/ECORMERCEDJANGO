# Generated by Django 4.1.3 on 2023-01-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0006_image_image_alter_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/categories/'),
        ),
    ]
