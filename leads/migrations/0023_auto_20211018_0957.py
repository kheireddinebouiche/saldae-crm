# Generated by Django 3.1 on 2021-10-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0022_auto_20211016_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='user_type',
            field=models.CharField(blank=True, choices=[('ad', 'Administrateur'), ('ag', 'Agent'), ('ve', 'Vendeur')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='categorie_client',
            field=models.CharField(blank=True, choices=[('p', 'Personne'), ('e', 'Entreprise')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='type_client',
            field=models.CharField(blank=True, choices=[('Fr', 'Fournisseur'), ('pr', 'Prospet'), ('cl', 'Client')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='etat',
            field=models.CharField(blank=True, choices=[('rep', 'Pause'), ('enc', 'En cours'), ('bro', 'Brouillon')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='methode_paiement',
            field=models.CharField(blank=True, choices=[('Virement', 'Virement'), ('Terme', 'A terme'), ('Cash', 'Cash')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='status',
            field=models.CharField(blank=True, choices=[('ann', 'Annullé'), ('fac', 'Facturé'), ('acc', 'Accepté'), ('env', 'Envoyé'), ('Ter', 'Terminé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('Youtube', 'Youtube'), ('Google', 'Google'), ('Newsletter', 'Newsletter')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='state',
            field=models.CharField(blank=True, choices=[('enc', 'En cours'), ('act', 'Active')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='produitsdevis',
            name='prix',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='produitsdevis',
            name='remise',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='produitsdevis',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='priorite',
            field=models.CharField(blank=True, choices=[('1', '1'), ('3', '3'), ('2', '2')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='status',
            field=models.CharField(blank=True, choices=[('aff', 'A faire'), ('enc', 'En cours'), ('enp', 'En pause'), ('ter', 'Terminé'), ('ann', 'Annulé')], max_length=3, null=True),
        ),
    ]
