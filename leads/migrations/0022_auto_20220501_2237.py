# Generated by Django 3.1 on 2022-05-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0021_auto_20220501_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigntache',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='assigntache',
            name='id_comp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assigntache',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='categorie_client',
            field=models.CharField(blank=True, choices=[('e', 'Entreprise'), ('p', 'Personne')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='type_client',
            field=models.CharField(blank=True, choices=[('cl', 'Client'), ('Fr', 'Fournisseur'), ('pr', 'Prospet')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='etat',
            field=models.CharField(blank=True, choices=[('bro', 'Brouillon'), ('enc', 'En cours'), ('rep', 'Pause'), ('sau', 'Sauvegarder')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='methode_paiement',
            field=models.CharField(blank=True, choices=[('Terme', 'A terme'), ('Virement', 'Virement'), ('Cash', 'Cash')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='status',
            field=models.CharField(blank=True, choices=[('env', 'Envoyé'), ('Ter', 'Terminé'), ('acc', 'Accepté'), ('ann', 'Annullé'), ('fac', 'Facturé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseurs',
            name='fournisseur_type',
            field=models.CharField(choices=[('pa', 'Paticulier'), ('en', 'Entreprise')], max_length=2),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='status',
            field=models.CharField(blank=True, choices=[('con', 'Confirmé'), ('att', 'En attante'), ('ann', 'Annulé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='priorite',
            field=models.CharField(blank=True, choices=[('3', '3'), ('1', '1'), ('2', '2')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='status',
            field=models.CharField(blank=True, choices=[('enc', 'En cours'), ('aff', 'A faire'), ('enp', 'En pause'), ('ter', 'Terminé'), ('ann', 'Annulé')], max_length=3, null=True),
        ),
    ]