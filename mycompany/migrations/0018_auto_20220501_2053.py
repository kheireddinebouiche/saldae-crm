# Generated by Django 3.1 on 2022-05-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycompany', '0017_auto_20220430_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycompany',
            name='niveau',
            field=models.CharField(blank=True, choices=[('pro', 'Pro.'), ('basic', 'Basic'), ('free', 'Free')], max_length=10, null=True),
        ),
    ]
