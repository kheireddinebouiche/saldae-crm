# Generated by Django 3.1 on 2022-04-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0004_auto_20220427_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('basic', 'Basic'), ('free', 'Free'), ('pro', 'Pro.')], max_length=10, null=True),
        ),
    ]
