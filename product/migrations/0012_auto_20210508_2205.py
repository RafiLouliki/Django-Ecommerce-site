# Generated by Django 3.2 on 2021-05-08 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0011_auto_20210508_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDIsBestSeller',
            field=models.BooleanField(default=False, verbose_name='Best Seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDIsNew',
            field=models.BooleanField(default=True, verbose_name='New Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product URL'),
        ),
    ]
