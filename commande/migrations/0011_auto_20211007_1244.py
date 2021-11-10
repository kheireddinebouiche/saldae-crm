# Generated by Django 3.1 on 2021-10-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0010_auto_20211007_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bondecommande',
            name='delai_paiement',
            field=models.CharField(blank=True, choices=[('atr', 'A terme'), ('30j', '30 Jours'), ('40j', '40 Jours'), ('60j', '60 Jours')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='bondecommande',
            name='status',
            field=models.CharField(blank=True, choices=[('val', 'Valider'), ('ann', 'Annuler'), ('con', 'Confirmer'), ('att', 'En attente')], max_length=3, null=True),
        ),
    ]