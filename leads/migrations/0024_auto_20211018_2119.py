# Generated by Django 3.1 on 2021-10-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0023_auto_20211018_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitsdevis',
            name='reference_product',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='user_type',
            field=models.CharField(blank=True, choices=[('ag', 'Agent'), ('ve', 'Vendeur'), ('ad', 'Administrateur')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='categorie_client',
            field=models.CharField(blank=True, choices=[('e', 'Entreprise'), ('p', 'Personne')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='etat',
            field=models.CharField(blank=True, choices=[('rep', 'Pause'), ('bro', 'Brouillon'), ('enc', 'En cours')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='methode_paiement',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Virement', 'Virement'), ('Terme', 'A terme')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='status',
            field=models.CharField(blank=True, choices=[('Ter', 'Terminé'), ('acc', 'Accepté'), ('ann', 'Annullé'), ('fac', 'Facturé'), ('env', 'Envoyé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('Google', 'Google'), ('Newsletter', 'Newsletter'), ('Youtube', 'Youtube')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='produitsdevis',
            name='prix',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='produitsdevis',
            name='remise',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='produitsdevis',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='priorite',
            field=models.CharField(blank=True, choices=[('3', '3'), ('2', '2'), ('1', '1')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='status',
            field=models.CharField(blank=True, choices=[('enp', 'En pause'), ('ann', 'Annulé'), ('ter', 'Terminé'), ('aff', 'A faire'), ('enc', 'En cours')], max_length=3, null=True),
        ),
    ]