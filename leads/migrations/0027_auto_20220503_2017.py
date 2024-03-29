# Generated by Django 3.1 on 2022-05-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0026_auto_20220502_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='motif',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='observation',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='user_type',
            field=models.CharField(blank=True, choices=[('ve', 'Vendeur'), ('ad', 'Administrateur'), ('ag', 'Agent')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='categorie_client',
            field=models.CharField(blank=True, choices=[('p', 'Personne'), ('e', 'Entreprise')], max_length=1, null=True),
        ),
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
            field=models.CharField(blank=True, choices=[('Terme', 'A terme'), ('Cash', 'Cash'), ('Virement', 'Virement')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='status',
            field=models.CharField(blank=True, choices=[('ann', 'Annullé'), ('env', 'Envoyé'), ('fac', 'Facturé'), ('acc', 'Accepté'), ('Ter', 'Terminé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseurs',
            name='fournisseur_type',
            field=models.CharField(choices=[('en', 'Entreprise'), ('pa', 'Paticulier')], max_length=2),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('Google', 'Google'), ('Youtube', 'Youtube'), ('Newsletter', 'Newsletter')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='state',
            field=models.CharField(blank=True, choices=[('enc', 'En cours'), ('act', 'Active')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='status',
            field=models.CharField(blank=True, choices=[('con', 'Confirmé'), ('att', 'En attante'), ('ann', 'Annulé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='priorite',
            field=models.CharField(blank=True, choices=[('2', '2'), ('1', '1'), ('3', '3')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='status',
            field=models.CharField(blank=True, choices=[('enc', 'En cours'), ('ter', 'Terminé'), ('enp', 'En pause'), ('ann', 'Annulé'), ('aff', 'A faire')], max_length=3, null=True),
        ),
    ]
