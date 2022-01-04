# Generated by Django 3.1 on 2022-01-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0027_auto_20220104_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bondecommande',
            name='delai_paiement',
            field=models.CharField(blank=True, choices=[('atr', 'A terme'), ('60j', '60 Jours'), ('30j', '30 Jours'), ('40j', '40 Jours')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='bondecommande',
            name='status',
            field=models.CharField(blank=True, choices=[('con', 'Confirmer'), ('att', 'En attente'), ('ann', 'Annuler'), ('val', 'Valider')], max_length=3, null=True),
        ),
    ]
