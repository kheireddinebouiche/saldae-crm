# Generated by Django 3.1 on 2022-05-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0024_auto_20220509_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('basic', 'Basic'), ('pro', 'Pro.'), ('free', 'Free')], max_length=10, null=True),
        ),
    ]