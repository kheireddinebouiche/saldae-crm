# Generated by Django 3.1 on 2022-05-01 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0020_auto_20220501_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='user_type',
            field=models.CharField(blank=True, choices=[('ad', 'Administrateur'), ('ve', 'Vendeur'), ('ag', 'Agent')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='assigntache',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.agent'),
        ),
        migrations.AlterField(
            model_name='client',
            name='categorie_client',
            field=models.CharField(blank=True, choices=[('p', 'Personne'), ('e', 'Entreprise')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='type_client',
            field=models.CharField(blank=True, choices=[('cl', 'Client'), ('pr', 'Prospet'), ('Fr', 'Fournisseur')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='etat',
            field=models.CharField(blank=True, choices=[('rep', 'Pause'), ('bro', 'Brouillon'), ('sau', 'Sauvegarder'), ('enc', 'En cours')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='methode_paiement',
            field=models.CharField(blank=True, choices=[('Virement', 'Virement'), ('Cash', 'Cash'), ('Terme', 'A terme')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='status',
            field=models.CharField(blank=True, choices=[('fac', 'Facturé'), ('acc', 'Accepté'), ('ann', 'Annullé'), ('env', 'Envoyé'), ('Ter', 'Terminé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseurs',
            name='fournisseur_type',
            field=models.CharField(choices=[('en', 'Entreprise'), ('pa', 'Paticulier')], max_length=2),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('Newsletter', 'Newsletter'), ('Youtube', 'Youtube'), ('Google', 'Google')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='state',
            field=models.CharField(blank=True, choices=[('act', 'Active'), ('enc', 'En cours')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='status',
            field=models.CharField(blank=True, choices=[('att', 'En attante'), ('ann', 'Annulé'), ('con', 'Confirmé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='priorite',
            field=models.CharField(blank=True, choices=[('2', '2'), ('1', '1'), ('3', '3')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='status',
            field=models.CharField(blank=True, choices=[('ter', 'Terminé'), ('enp', 'En pause'), ('aff', 'A faire'), ('ann', 'Annulé'), ('enc', 'En cours')], max_length=3, null=True),
        ),
    ]
