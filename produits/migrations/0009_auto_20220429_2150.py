# Generated by Django 3.1 on 2022-04-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0008_auto_20220429_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouvementstock',
            name='type_operation',
            field=models.CharField(blank=True, choices=[('e', 'Entrer'), ('s', 'Sortie')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='cat_produit',
            field=models.CharField(blank=True, choices=[('prd', 'Produits'), ('srv', 'Service')], max_length=3, null=True),
        ),
    ]
