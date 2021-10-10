# Generated by Django 3.2 on 2021-05-01 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='CATparent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATparent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALNAlternative', models.ManyToManyField(related_name='alternative_product', to='product.Product')),
                ('PALNProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product')),
            ],
            options={
                'verbose_name': 'Product_Alternative',
                'verbose_name_plural': 'Product_Alternatives',
            },
        ),
    ]