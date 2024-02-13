# Generated by Django 3.1 on 2022-04-29 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0005_auto_20220428_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='id_company',
            field=models.IntegerField(blank=True, null=True),
        ),
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
