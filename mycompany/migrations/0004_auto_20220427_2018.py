# Generated by Django 3.1 on 2022-04-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0003_auto_20220425_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('pro', 'Pro.'), ('basic', 'Basic'), ('free', 'Free')], max_length=10, null=True),
        ),
    ]
