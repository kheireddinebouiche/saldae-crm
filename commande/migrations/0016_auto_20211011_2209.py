# Generated by Django 3.1 on 2021-10-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0015_auto_20211011_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bondecommande',
            name='delai_paiement',
            field=models.CharField(blank=True, choices=[('60j', '60 Jours'), ('atr', 'A terme'), ('30j', '30 Jours'), ('40j', '40 Jours')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='bondecommande',
            name='status',
            field=models.CharField(blank=True, choices=[('att', 'En attente'), ('ann', 'Annuler'), ('con', 'Confirmer'), ('val', 'Valider')], max_length=3, null=True),
        ),
    ]