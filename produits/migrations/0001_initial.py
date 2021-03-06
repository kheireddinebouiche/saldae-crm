# Generated by Django 3.1.4 on 2021-08-22 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Typeproduit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, max_length=1000, null=True)),
                ('designation', models.CharField(blank=True, max_length=1000, null=True)),
                ('cat_produit', models.CharField(blank=True, choices=[('prd', 'Produits'), ('srv', 'Service')], max_length=3, null=True)),
                ('couleur', models.CharField(blank=True, max_length=100, null=True)),
                ('poids', models.FloatField(blank=True, null=True)),
                ('longueur', models.FloatField(blank=True, null=True)),
                ('largeur', models.FloatField(blank=True, null=True)),
                ('prix', models.FloatField(blank=True, null=True)),
                ('type_produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produits.typeproduit')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
        ),
    ]
