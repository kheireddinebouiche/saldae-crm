# Generated by Django 3.1 on 2021-10-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0006_produit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='promo',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
