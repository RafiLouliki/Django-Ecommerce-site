# Generated by Django 3.2 on 2021-05-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_prdimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
