# Generated by Django 3.1 on 2021-09-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0002_auto_20210905_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='cat_produit',
            field=models.CharField(blank=True, choices=[('prd', 'Produits'), ('srv', 'Service')], max_length=3, null=True),
        ),
    ]
