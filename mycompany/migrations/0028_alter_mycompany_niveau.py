# Generated by Django 4.1.5 on 2023-01-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0027_auto_20220512_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('pro', 'Pro.'), ('basic', 'Basic'), ('free', 'Free')], max_length=10, null=True),
        ),
    ]
