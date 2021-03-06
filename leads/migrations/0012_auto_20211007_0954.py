# Generated by Django 3.1 on 2021-10-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20211006_1423'),
    ]

    operations = [
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
            name='status',
            field=models.CharField(blank=True, choices=[('acc', 'Accepté'), ('env', 'Envoyé'), ('Ter', 'Terminé'), ('ann', 'Annullé'), ('fac', 'Facturé')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='fournisseurs',
            name='fournisseur_type',
            field=models.CharField(choices=[('pa', 'Paticulier'), ('en', 'Entreprise')], max_length=2),
        ),
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('Google', 'Google'), ('Newsletter', 'Newsletter'), ('Youtube', 'Youtube')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='state',
            field=models.CharField(blank=True, choices=[('act', 'Active'), ('enc', 'En cours')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='tache',
            name='priorite',
            field=models.CharField(blank=True, choices=[('2', '2'), ('1', '1'), ('3', '3')], max_length=1, null=True),
        ),
    ]
