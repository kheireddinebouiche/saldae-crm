# Generated by Django 3.1 on 2022-01-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0025_auto_20220102_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bondecommande',
            name='delai_paiement',
            field=models.CharField(blank=True, choices=[('60j', '60 Jours'), ('40j', '40 Jours'), ('30j', '30 Jours'), ('atr', 'A terme')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='bondecommande',
            name='status',
            field=models.CharField(blank=True, choices=[('att', 'En attente'), ('con', 'Confirmer'), ('val', 'Valider'), ('ann', 'Annuler')], max_length=3, null=True),
        ),
    ]