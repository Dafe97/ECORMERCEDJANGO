# Generated by Django 4.1.3 on 2023-01-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_alter_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ImageField(blank=True, null=True, upload_to='images/products'),
        ),
    ]
