# Generated by Django 3.1 on 2022-04-23 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('hauteur', models.FloatField(blank=True, null=True)),
                ('prix', models.FloatField(blank=True, null=True)),
                ('promo', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
        ),
        migrations.CreateModel(
            name='Typeproduit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.FloatField(blank=True, null=True)),
                ('lot', models.CharField(blank=True, max_length=100, null=True)),
                ('date_fabrication', models.DateField(blank=True, null=True)),
                ('date_peremption', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('produit', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='produits.produit')),
            ],
            options={
                'verbose_name': 'Stock produit',
                'verbose_name_plural': 'Stock de produits',
            },
        ),
        migrations.AddField(
            model_name='produit',
            name='type_produit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produits.typeproduit'),
        ),
        migrations.CreateModel(
            name='MouvementStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_operation', models.DateTimeField(blank=True, null=True)),
                ('type_operation', models.CharField(blank=True, choices=[('s', 'Sortie'), ('e', 'Entrer')], max_length=2, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='produits.produit')),
            ],
            options={
                'verbose_name': 'Mouvement de stock',
                'verbose_name_plural': 'Mouvements de stock',
            },
        ),
    ]
