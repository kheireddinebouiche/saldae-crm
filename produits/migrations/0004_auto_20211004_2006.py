# Generated by Django 3.1 on 2021-10-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_auto_20210908_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='cat_produit',
            field=models.CharField(blank=True, choices=[('srv', 'Service'), ('prd', 'Produits')], max_length=3, null=True),
        ),
    ]