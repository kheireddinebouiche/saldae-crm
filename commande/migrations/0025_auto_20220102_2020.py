# Generated by Django 3.1 on 2022-01-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0024_auto_20220102_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bondecommande',
            name='delai_paiement',
            field=models.CharField(blank=True, choices=[('atr', 'A terme'), ('40j', '40 Jours'), ('60j', '60 Jours'), ('30j', '30 Jours')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='bondecommande',
            name='status',
            field=models.CharField(blank=True, choices=[('val', 'Valider'), ('con', 'Confirmer'), ('att', 'En attente'), ('ann', 'Annuler')], max_length=3, null=True),
        ),
    ]