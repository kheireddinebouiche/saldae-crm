# Generated by Django 3.1 on 2022-04-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0004_auto_20220427_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouvementstock',
            name='type_operation',
            field=models.CharField(blank=True, choices=[('s', 'Sortie'), ('e', 'Entrer')], max_length=2, null=True),
        ),
    ]
