# Generated by Django 3.2 on 2021-05-01 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210501_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATname', models.CharField(max_length=50)),
                ('CATdesc', models.TextField()),
                ('CATimg', models.ImageField(upload_to='category/')),
                ('CATparent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
