# Generated by Django 3.1 on 2022-04-30 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20220430_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='id_comp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='user_type',
            field=models.CharField(blank=True, choices=[('ag', 'Agent'), ('ad', 'Administrateur'), ('ve', 'Vendeur')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='type_client',
            field=models.CharField(blank=True, choices=[('Fr', 'Fournisseur'), ('pr', 'Prospet'), ('cl', 'Client')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='etat',
            field=models.CharField(blank=True, choices=[('bro', 'Brouillon'), ('enc', 'En cours'), ('rep', 'Pause'), ('sau', 'Sauvegarder')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='methode_paiement',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Virement', 'Virement'), ('Terme', 'A terme')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='status',
            field=models.CharField(blank=True, choices=[('Ter', 'Terminé'), ('env', 'Envoyé'), ('ann', 'Annullé'), ('acc', 'Accepté'), ('fac', 'Facturé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseurs',
            name='fournisseur_type',
            field=models.CharField(choices=[('en', 'Entreprise'), ('pa', 'Paticulier')], max_length=2),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('Newsletter', 'Newsletter'), ('Google', 'Google'), ('Youtube', 'Youtube')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='status',
            field=models.CharField(blank=True, choices=[('con', 'Confirmé'), ('att', 'En attante'), ('ann', 'Annulé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='priorite',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='status',
            field=models.CharField(blank=True, choices=[('aff', 'A faire'), ('ter', 'Terminé'), ('enc', 'En cours'), ('enp', 'En pause'), ('ann', 'Annulé')], max_length=3, null=True),
        ),
    ]
