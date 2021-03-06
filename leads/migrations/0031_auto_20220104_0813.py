# Generated by Django 3.1 on 2022-01-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0030_auto_20220104_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='type_client',
            field=models.CharField(blank=True, choices=[('pr', 'Prospet'), ('Fr', 'Fournisseur'), ('cl', 'Client')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='etat',
            field=models.CharField(blank=True, choices=[('bro', 'Brouillon'), ('sau', 'Sauvegarder'), ('enc', 'En cours'), ('rep', 'Pause')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='methode_paiement',
            field=models.CharField(blank=True, choices=[('Terme', 'A terme'), ('Virement', 'Virement'), ('Cash', 'Cash')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='status',
            field=models.CharField(blank=True, choices=[('acc', 'Accepté'), ('ann', 'Annullé'), ('env', 'Envoyé'), ('Ter', 'Terminé'), ('fac', 'Facturé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseurs',
            name='fournisseur_type',
            field=models.CharField(choices=[('pa', 'Paticulier'), ('en', 'Entreprise')], max_length=2),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('Youtube', 'Youtube'), ('Google', 'Google'), ('Newsletter', 'Newsletter')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='status',
            field=models.CharField(blank=True, choices=[('ter', 'Terminé'), ('aff', 'A faire'), ('ann', 'Annulé'), ('enc', 'En cours'), ('enp', 'En pause')], max_length=3, null=True),
        ),
    ]
